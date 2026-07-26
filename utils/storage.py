"""Lightweight local storage for bookings.

Streamlit Community Cloud's free tier doesn't guarantee this SQLite file
survives an app restart/redeploy, so this is a "nice to have" record —
the real backstop is the notification email sent to Dave on every booking
(see email_utils.send_booking_emails).
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "bookings.db"


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                restaurant TEXT NOT NULL,
                party_size INTEGER NOT NULL,
                reservation_time TEXT NOT NULL,
                guest_name TEXT NOT NULL,
                guest_email TEXT NOT NULL,
                confirmation_code TEXT NOT NULL,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            )
            """
        )


def save_booking(
    restaurant: str,
    party_size: int,
    reservation_time: str,
    guest_name: str,
    guest_email: str,
    confirmation_code: str,
) -> None:
    init_db()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO bookings
                (restaurant, party_size, reservation_time, guest_name, guest_email, confirmation_code)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (restaurant, party_size, reservation_time, guest_name, guest_email, confirmation_code),
        )
