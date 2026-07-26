"""Date-night event facts and time calculations.

All of these numbers are for one specific, fixed trip (Vacaville -> downtown
Sacramento) on one specific night, so we hardcode a researched drive time
instead of calling a live maps/traffic API. That keeps the whole app free
and free of API keys.
"""

from datetime import date, datetime, time, timedelta

EVENT_DATE = date(2026, 8, 1)  # Saturday
SHOWTIME = time(18, 30)
MOVIE_TITLE = "The Odyssey"

THEATER_NAME = "Esquire IMAX Theatre"
THEATER_ADDRESS = "1211 K St, Sacramento, CA 95814"
HOME_ADDRESS = "518 Aliki Dr, Vacaville, CA 95688"

# Researched: Vacaville -> downtown Sacramento via I-80 is ~33-37 min in
# typical traffic.
DRIVE_MINUTES = 37
# Extra time to find downtown parking and walk in on a Saturday evening.
PARKING_AND_WALK_BUFFER_MINUTES = 15
# General safety margin.
SAFETY_MARGIN_MINUTES = 10

DINNER_DURATION_MINUTES = 75
# How long before the movie starts they should be at the theater.
THEATER_ARRIVAL_BUFFER_MINUTES = 15


def _round_down_to_quarter_hour(dt: datetime) -> datetime:
    discard = timedelta(minutes=dt.minute % 15, seconds=dt.second, microseconds=dt.microsecond)
    return dt - discard


def showtime_datetime() -> datetime:
    return datetime.combine(EVENT_DATE, SHOWTIME)


def suggested_reservation_time(walk_minutes: int) -> datetime:
    """Back-calculate a sensible dinner reservation time for a given
    restaurant's walk time to the theater."""
    latest_theater_arrival = showtime_datetime() - timedelta(minutes=THEATER_ARRIVAL_BUFFER_MINUTES)
    latest_dinner_end = latest_theater_arrival - timedelta(minutes=walk_minutes)
    suggested_start = latest_dinner_end - timedelta(minutes=DINNER_DURATION_MINUTES)
    return _round_down_to_quarter_hour(suggested_start)


def time_options(center: datetime, span_minutes: int = 45, step_minutes: int = 15) -> list[datetime]:
    """A small list of selectable reservation times around a suggested time."""
    start = center - timedelta(minutes=span_minutes)
    count = (span_minutes * 2) // step_minutes + 1
    return [start + timedelta(minutes=i * step_minutes) for i in range(count)]


def leave_home_by(reservation_dt: datetime) -> datetime:
    total_buffer = DRIVE_MINUTES + PARKING_AND_WALK_BUFFER_MINUTES + SAFETY_MARGIN_MINUTES
    return reservation_dt - timedelta(minutes=total_buffer)


def format_friendly(dt: datetime) -> str:
    """Cross-platform 'Saturday, August 1 at 4:45 PM' formatting
    (avoids %-d / %-I strftime flags, which aren't supported on Windows)."""
    time_str = dt.strftime("%I:%M %p")
    if time_str.startswith("0"):
        time_str = time_str[1:]
    return f"{dt.strftime('%A, %B')} {dt.day} at {time_str}"
