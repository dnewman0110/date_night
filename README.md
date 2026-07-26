# Date Night 🍷

A small personal gift app: Allison picks the restaurant, browses the menu,
picks a dinner time, and reserves it before your Aug 1, 2026 date night
(*The Odyssey*, 6:30 PM, Esquire IMAX Theatre). It emails her a confirmation
and works out what time you need to leave the house.

Neither OpenTable nor Tock offer a public API for third-party apps to pull
live availability or submit bookings, so this app doesn't book automatically.
Instead, each restaurant's booking step deep-links to its real reservation
page (OpenTable for Ella and Frank Fat's, Tock for the Firehouse) with the
date, time, and party size pre-filled where the platform allows it. Allison
completes the actual reservation there, then comes back and pastes in the
confirmation number so the app can save it and email you both.

## Run it locally

```
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
streamlit run app.py
```

Without secrets configured (see below), the app still works end-to-end —
it just won't be able to send emails, and will say so on the confirmation
screen instead of erroring out.

## Deploying (free, on Streamlit Community Cloud)

1. Push this repo to GitHub (already wired up as `origin` →
   `https://github.com/dnewman0110/date_night`):
   ```
   git add .
   git commit -m "Date night app"
   git push -u origin main
   ```
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in with
   GitHub, click **New app**, and point it at this repo's `app.py`.
3. Once deployed, open the app's **Settings → Secrets** and paste in:
   ```toml
   SMTP_EMAIL = "dave24188@gmail.com"
   SMTP_APP_PASSWORD = "xxxx xxxx xxxx xxxx"
   NOTIFY_EMAIL = "dave24188@gmail.com"
   ```
4. Reboot the app from the Streamlit Cloud dashboard so the new secrets
   take effect.

### Getting a Gmail App Password (for `SMTP_APP_PASSWORD`)

Gmail won't accept your normal password for this — you need a 16-character
**App Password**, which requires 2-Step Verification to be turned on:

1. Turn on 2-Step Verification: [myaccount.google.com/security](https://myaccount.google.com/security)
2. Then go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
3. Create a new app password (name it anything, e.g. "Date Night App")
4. Copy the 16-character password it gives you — that's `SMTP_APP_PASSWORD`
   (spaces don't matter)

## Before Saturday

Send yourself a real test booking through the deployed app first, to
confirm both the guest confirmation email and your notification email
actually arrive.
