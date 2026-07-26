import random
import string

import streamlit as st

from data.restaurants import RESTAURANTS, get_restaurant
from data.reviews import REVIEWS
from utils import reservations, scheduling
from utils.email_utils import send_booking_emails
from utils.storage import save_booking

st.set_page_config(
    page_title="Date Night — Allison & Dave",
    page_icon="🍷",
    layout="centered",
)

CSS = """
<style>
:root { color-scheme: light; }
#MainMenu, footer, header {visibility: hidden;}
.block-container {max-width: 560px; padding-top: 2rem; padding-bottom: 3rem;}

html, body, [class*="css"] { font-family: Georgia, 'Times New Roman', serif; }

.dn-hero {
    text-align: center;
    padding: 1.5rem 1rem 1rem 1rem;
}
.dn-hero h1 {
    font-size: 2rem;
    color: #6b1f2a;
    margin-bottom: 0.25rem;
}
.dn-hero p { color: #6b5f52; font-size: 1.05rem; }

.dn-card {
    border: 1px solid #e5ded2;
    border-radius: 14px;
    padding: 1.1rem 1.2rem;
    margin-bottom: 1.1rem;
    background: #fffdf9;
}
.dn-card h3 { margin: 0 0 0.15rem 0; color: #2f2a24; }
.dn-meta { color: #8a7c68; font-size: 0.9rem; margin-bottom: 0.5rem; }
.dn-blurb { color: #4a443b; margin-bottom: 0.5rem; }

.dn-menu-section { font-weight: bold; color: #6b1f2a; margin-top: 0.6rem; }
.dn-menu-item { margin: 0.25rem 0; color: #2f2a24; }
.dn-menu-item .price { float: right; color: #8a7c68; }
.dn-menu-desc { color: #8a7c68; font-size: 0.85rem; }

.dn-summary-box {
    background: #f6efe3;
    border-radius: 12px;
    padding: 1rem 1.2rem;
    margin: 1rem 0;
}

.dn-review {
    border: 1px solid #e5ded2;
    border-radius: 14px;
    padding: 1rem 1.2rem;
    margin-bottom: 0.9rem;
    background: #fffdf9;
}
.dn-review blockquote {
    margin: 0 0 0.5rem 0;
    font-style: italic;
    color: #2f2a24;
    font-size: 1.05rem;
}
.dn-review .attribution { color: #8a7c68; font-size: 0.9rem; }
.dn-review-mock {
    background: #f6efe3;
    border: 1px solid #d8c7a8;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    background: #6b1f2a;
    color: white;
    border: none;
    padding: 0.6rem 0;
}
.stButton>button:hover { background: #591a23; color: white; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

if "step" not in st.session_state:
    st.session_state.step = "welcome"
if "selected_restaurant_id" not in st.session_state:
    st.session_state.selected_restaurant_id = None
if "selected_time" not in st.session_state:
    st.session_state.selected_time = None
if "booking" not in st.session_state:
    st.session_state.booking = None


def go_to(step: str) -> None:
    st.session_state.step = step
    st.rerun()


def render_welcome() -> None:
    st.markdown(
        f"""
        <div class="dn-hero">
            <h1>Hi Allison 💛</h1>
            <p>You deserve a night out — so I planned one, and I want you to
            pick the details.</p>
        </div>
        <div class="dn-summary-box">
            <b>🎬 {scheduling.MOVIE_TITLE}</b><br/>
            {scheduling.format_friendly(scheduling.showtime_datetime())}<br/>
            {scheduling.THEATER_NAME}, {scheduling.THEATER_ADDRESS}
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("First things first — where should we eat beforehand?")
    if st.button("Let's plan our night →"):
        go_to("restaurant")
    if st.button("📰 See what critics are saying about the movie"):
        go_to("reviews")


def render_reviews() -> None:
    st.header(f"Reviews of {scheduling.MOVIE_TITLE}")
    st.caption("One from Dave, the rest from actual film critics.")

    for review in REVIEWS:
        card_class = "dn-review dn-review-mock" if review.get("mock") else "dn-review"
        emoji = "💌" if review.get("mock") else ("🍅" if review.get("critical") else "🎬")
        st.markdown(
            f"""
            <div class="{card_class}">
                <blockquote>{emoji} "{review['quote']}"</blockquote>
                <div class="attribution">— {review['author']}, {review['source']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.write("")
    if st.button("← Back", key="back_to_welcome_from_reviews"):
        go_to("welcome")


def render_restaurant_menu(restaurant: dict) -> None:
    for section, items in restaurant["menu"].items():
        st.markdown(f'<div class="dn-menu-section">{section}</div>', unsafe_allow_html=True)
        for name, desc, price in items:
            st.markdown(
                f"""
                <div class="dn-menu-item">
                    <span class="price">{price}</span>
                    <b>{name}</b>
                    <div class="dn-menu-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_restaurant_selection() -> None:
    st.header("Pick a restaurant")
    st.caption(f"All an easy walk from {scheduling.THEATER_NAME}")

    for restaurant in RESTAURANTS:
        st.markdown(
            f"""
            <div class="dn-card">
                <h3>{restaurant['name']}</h3>
                <div class="dn-meta">
                    {restaurant['cuisine']} · {restaurant['price_range']} ·
                    ⭐ {restaurant['rating']} · 🚶 {restaurant['walk_minutes']} min to the theater
                </div>
                <div class="dn-blurb">{restaurant['blurb']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.expander(f"View {restaurant['name']}'s menu"):
            render_restaurant_menu(restaurant)
        if st.button(f"Choose {restaurant['name']}", key=f"choose_{restaurant['id']}"):
            st.session_state.selected_restaurant_id = restaurant["id"]
            go_to("time")

    st.write("")
    if st.button("← Back", key="back_to_welcome"):
        go_to("welcome")


def render_time_selection() -> None:
    restaurant = get_restaurant(st.session_state.selected_restaurant_id)
    st.header(f"Dinner at {restaurant['name']}")

    suggested = scheduling.suggested_reservation_time(restaurant["walk_minutes"])
    options = scheduling.time_options(suggested)
    labels = [scheduling.format_friendly(t) for t in options]
    suggested_label = scheduling.format_friendly(suggested)

    st.write(
        f"To make the {scheduling.format_friendly(scheduling.showtime_datetime())} showing "
        f"comfortably, we recommend a reservation around **{suggested_label}**."
    )

    chosen_label = st.radio("Pick a reservation time:", labels, index=labels.index(suggested_label))
    chosen_time = options[labels.index(chosen_label)]

    if st.button("Confirm this time →"):
        st.session_state.selected_time = chosen_time
        go_to("booking")

    if st.button("← Back", key="back_to_restaurant"):
        go_to("restaurant")


def render_booking_form() -> None:
    restaurant = get_restaurant(st.session_state.selected_restaurant_id)
    time_label = scheduling.format_friendly(st.session_state.selected_time)
    platform_name = reservations.platform_label(restaurant)

    st.header("Almost there")
    st.markdown(
        f"""
        <div class="dn-summary-box">
            <b>{restaurant['name']}</b><br/>
            {time_label}<br/>
            {restaurant['address']}
        </div>
        """,
        unsafe_allow_html=True,
    )

    party_size = st.number_input("Party size", min_value=1, max_value=8, value=2, step=1, key="party_size_input")
    deep_link = reservations.build_deep_link(restaurant, st.session_state.selected_time, int(party_size))

    st.markdown(f"**Step 1 — reserve the table on {platform_name}**")
    st.write(
        f"This app can't book on {platform_name} for you — there's no public API for that — "
        f"but it can take you straight to {restaurant['name']}'s real reservation page with "
        f"{time_label} and a party of {int(party_size)} pre-filled. Grab whatever time actually "
        f"shows available there."
    )
    if deep_link:
        st.link_button(f"Reserve on {platform_name} →", deep_link)
    else:
        st.info(f"Call {restaurant['name']} directly to reserve at {restaurant['address']}.")

    st.markdown("**Step 2 — save it here**")
    st.write("Once you've got a real reservation, fill this in so it's saved and you get an email.")

    with st.form("booking_form"):
        name = st.text_input("Name for the reservation", value="Allison")
        email = st.text_input("Email for your confirmation")
        confirmation_code = st.text_input(
            f"Confirmation number from {platform_name} (optional)",
            help=f"Paste the confirmation number {platform_name} gave you, if any.",
        )
        submitted = st.form_submit_button("Save My Reservation")

    if submitted:
        if not name.strip() or "@" not in email:
            st.error("Please enter your name and a valid email address.")
            return

        confirmed_externally = bool(confirmation_code.strip())
        code = confirmation_code.strip() or (
            "DN-" + "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
        )
        reservation_dt = st.session_state.selected_time
        leave_by = scheduling.leave_home_by(reservation_dt)

        try:
            save_booking(
                restaurant=restaurant["name"],
                party_size=int(party_size),
                reservation_time=time_label,
                guest_name=name.strip(),
                guest_email=email.strip(),
                confirmation_code=code,
            )
        except Exception:
            pass  # local storage is a bonus; the notification email is the real backstop

        notify_email = st.secrets.get("NOTIFY_EMAIL", "")
        email_result = send_booking_emails(
            guest_name=name.strip(),
            guest_email=email.strip(),
            restaurant_name=restaurant["name"],
            restaurant_address=restaurant["address"],
            reservation_time_str=time_label,
            party_size=int(party_size),
            confirmation_code=code,
            notify_email=notify_email,
            leave_by_str=scheduling.format_friendly(leave_by),
            confirmed_externally=confirmed_externally,
            platform_name=platform_name,
        )

        st.session_state.booking = {
            "restaurant": restaurant,
            "name": name.strip(),
            "email": email.strip(),
            "party_size": int(party_size),
            "reservation_dt": reservation_dt,
            "confirmation_code": code,
            "confirmed_externally": confirmed_externally,
            "leave_by": leave_by,
            "email_result": email_result,
        }
        go_to("confirmation")

    if st.button("← Back", key="back_to_time"):
        go_to("time")


def render_confirmation() -> None:
    b = st.session_state.booking
    restaurant = b["restaurant"]
    time_label = scheduling.format_friendly(b["reservation_dt"])
    leave_by_label = scheduling.format_friendly(b["leave_by"])
    platform_name = reservations.platform_label(restaurant)
    code_label = f"{platform_name} Confirmation #" if b["confirmed_externally"] else "Reference #"

    st.markdown(
        f"""
        <div class="dn-hero">
            <h1>🎉 Reservation Confirmed</h1>
        </div>
        <div class="dn-card">
            <h3>{restaurant['name']}</h3>
            <div class="dn-meta">{restaurant['address']}</div>
            <table style="width:100%; margin-top: 0.5rem;">
                <tr><td style="color:#8a7c68;">Date &amp; Time</td>
                    <td style="text-align:right; font-weight:bold;">{time_label}</td></tr>
                <tr><td style="color:#8a7c68;">Party Size</td>
                    <td style="text-align:right; font-weight:bold;">{b['party_size']}</td></tr>
                <tr><td style="color:#8a7c68;">{code_label}</td>
                    <td style="text-align:right; font-weight:bold;">{b['confirmation_code']}</td></tr>
            </table>
        </div>
        <div class="dn-summary-box">
            🎬 {scheduling.MOVIE_TITLE} — {scheduling.format_friendly(scheduling.showtime_datetime())}<br/>
            {scheduling.THEATER_NAME}, {scheduling.THEATER_ADDRESS}
        </div>
        <div class="dn-summary-box">
            🚗 <b>Leave home by {leave_by_label}</b><br/>
            <span style="color:#8a7c68; font-size:0.9rem;">
            From {scheduling.HOME_ADDRESS} — based on a typical ~{scheduling.DRIVE_MINUTES} min
            drive via I-80 plus time to park and walk in. Check live traffic before you go.
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if b["email_result"]["guest_ok"]:
        st.success(f"A confirmation email is on its way to {b['email']}.")
    else:
        st.info("Your reservation is saved! (We couldn't send a confirmation email right now.)")

    if not b["confirmed_externally"]:
        st.warning(
            f"No {platform_name} confirmation number was entered — make sure the reservation "
            f"actually went through before you head out."
        )

    st.caption("Can't wait for date night. ❤️")


if st.session_state.step == "welcome":
    render_welcome()
elif st.session_state.step == "reviews":
    render_reviews()
elif st.session_state.step == "restaurant":
    render_restaurant_selection()
elif st.session_state.step == "time":
    render_time_selection()
elif st.session_state.step == "booking":
    render_booking_form()
elif st.session_state.step == "confirmation":
    render_confirmation()
