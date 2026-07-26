"""Deep links into each restaurant's real reservation platform.

There's no public API that lets a third-party app like this one pull live
table availability or submit a booking on OpenTable's or Tock's behalf —
that access is restricted to restaurants and approved reservation partners.
So instead of faking a booking, we hand off to the restaurant's real
reservation page with the date, time, and party size pre-filled where the
platform supports it. The guest completes the actual reservation there,
then comes back to this app to save the details and get an email.
"""

from datetime import datetime

PLATFORM_LABELS = {
    "opentable": "OpenTable",
    "tock": "Tock",
}


def platform_label(restaurant: dict) -> str:
    return PLATFORM_LABELS.get(restaurant.get("reservation_platform"), "the restaurant's site")


def build_deep_link(restaurant: dict, reservation_dt: datetime, party_size: int) -> str:
    """Best-effort deep link with date/time/party size pre-filled.

    Neither OpenTable nor Tock publish these query parameters, so this is
    based on patterns observed in the wild rather than documented behavior.
    If a platform ignores them, the link still lands on the right
    restaurant's real reservation page.
    """
    base_url = restaurant.get("reservation_url")
    if not base_url:
        return ""

    platform = restaurant.get("reservation_platform")
    date_str = reservation_dt.strftime("%Y-%m-%d")
    time_str = reservation_dt.strftime("%H:%M")
    sep = "&" if "?" in base_url else "?"

    if platform == "opentable":
        return f"{base_url}{sep}covers={party_size}&dateTime={date_str}T{time_str}"
    if platform == "tock":
        return f"{base_url}{sep}size={party_size}&date={date_str}&time={time_str}"
    return base_url
