"""Sends the guest confirmation email and a backup notification email to
Dave, using Gmail SMTP. Credentials come from Streamlit secrets and are
never hardcoded.

Both sends are best-effort: if SMTP isn't configured or fails, the caller
still keeps the booking (see storage.py) and the UI shows a friendly
message rather than crashing.
"""

import smtplib
import ssl
from email.message import EmailMessage

import streamlit as st

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


def _smtp_configured() -> bool:
    return "SMTP_EMAIL" in st.secrets and "SMTP_APP_PASSWORD" in st.secrets


def _send(to_addr: str, subject: str, html_body: str) -> tuple[bool, str]:
    if not _smtp_configured():
        return False, "Email isn't configured yet (missing SMTP secrets)."

    sender = st.secrets["SMTP_EMAIL"]
    password = st.secrets["SMTP_APP_PASSWORD"]

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = f"Date Night Reservations <{sender}>"
    msg["To"] = to_addr
    msg.set_content("This email requires an HTML-capable email client to view.")
    msg.add_alternative(html_body, subtype="html")

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
            server.login(sender, password)
            server.send_message(msg)
        return True, ""
    except Exception as exc:  # noqa: BLE001 - surfaced to the UI, not swallowed
        return False, str(exc)


def guest_confirmation_html(
    guest_name: str,
    restaurant_name: str,
    restaurant_address: str,
    reservation_time_str: str,
    party_size: int,
    confirmation_code: str,
    confirmed_externally: bool,
    platform_name: str,
) -> str:
    code_label = f"{platform_name} Confirmation #" if confirmed_externally else "Reference #"
    booked_via_line = (
        f"<p>Reserved via {platform_name}. Here's a copy of the details for your records:</p>"
        if confirmed_externally
        else "<p>Here are your reservation details:</p>"
    )
    return f"""
    <div style="font-family: Georgia, 'Times New Roman', serif; max-width: 480px;
                margin: 0 auto; border: 1px solid #e2ddd3; border-radius: 12px;
                overflow: hidden;">
      <div style="background: #2f2a24; color: #f6efe3; padding: 24px; text-align: center;">
        <div style="letter-spacing: 3px; font-size: 12px; text-transform: uppercase;
                    color: #cdbfa5;">Reservation Confirmed</div>
        <div style="font-size: 22px; margin-top: 6px;">{restaurant_name}</div>
      </div>
      <div style="padding: 24px; color: #2f2a24;">
        <p>Hi {guest_name},</p>
        {booked_via_line}
        <table style="width: 100%; border-collapse: collapse; margin: 16px 0;">
          <tr><td style="padding: 6px 0; color: #7a7267;">Date &amp; Time</td>
              <td style="padding: 6px 0; text-align: right; font-weight: bold;">{reservation_time_str}</td></tr>
          <tr><td style="padding: 6px 0; color: #7a7267;">Party Size</td>
              <td style="padding: 6px 0; text-align: right; font-weight: bold;">{party_size}</td></tr>
          <tr><td style="padding: 6px 0; color: #7a7267;">Location</td>
              <td style="padding: 6px 0; text-align: right; font-weight: bold;">{restaurant_address}</td></tr>
          <tr><td style="padding: 6px 0; color: #7a7267;">{code_label}</td>
              <td style="padding: 6px 0; text-align: right; font-weight: bold;">{confirmation_code}</td></tr>
        </table>
        <p style="color: #7a7267; font-size: 14px;">We look forward to serving you. See you soon!</p>
      </div>
    </div>
    """


def dave_notification_html(
    guest_name: str,
    restaurant_name: str,
    reservation_time_str: str,
    party_size: int,
    guest_email: str,
    confirmation_code: str,
    leave_by_str: str,
    confirmed_externally: bool,
    platform_name: str,
) -> str:
    if confirmed_externally:
        status_line = f"Reservation confirmed via {platform_name}."
    else:
        status_line = (
            f"No confirmation number was entered — double-check this reservation "
            f"actually went through on {platform_name} (or call the restaurant directly)."
        )
    return f"""
    <div style="font-family: Arial, sans-serif; max-width: 480px; margin: 0 auto;">
      <h2>Allison booked date night!</h2>
      <p><b>Restaurant:</b> {restaurant_name}</p>
      <p><b>Reservation time:</b> {reservation_time_str}</p>
      <p><b>Party size:</b> {party_size}</p>
      <p><b>Booked under:</b> {guest_name} ({guest_email})</p>
      <p><b>Confirmation code:</b> {confirmation_code}</p>
      <p><b>Suggested leave-home time:</b> {leave_by_str}</p>
      <p style="color:#777;">{status_line}</p>
    </div>
    """


def send_booking_emails(
    guest_name: str,
    guest_email: str,
    restaurant_name: str,
    restaurant_address: str,
    reservation_time_str: str,
    party_size: int,
    confirmation_code: str,
    notify_email: str,
    leave_by_str: str,
    confirmed_externally: bool,
    platform_name: str,
) -> dict:
    guest_ok, guest_err = _send(
        guest_email,
        f"Your reservation at {restaurant_name} is confirmed",
        guest_confirmation_html(
            guest_name,
            restaurant_name,
            restaurant_address,
            reservation_time_str,
            party_size,
            confirmation_code,
            confirmed_externally,
            platform_name,
        ),
    )

    notify_ok, notify_err = False, ""
    if notify_email:
        notify_ok, notify_err = _send(
            notify_email,
            f"Allison booked {restaurant_name} for date night",
            dave_notification_html(
                guest_name,
                restaurant_name,
                reservation_time_str,
                party_size,
                guest_email,
                confirmation_code,
                leave_by_str,
                confirmed_externally,
                platform_name,
            ),
        )

    return {
        "guest_ok": guest_ok,
        "guest_err": guest_err,
        "notify_ok": notify_ok,
        "notify_err": notify_err,
    }
