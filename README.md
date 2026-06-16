# UNI TRAVEL MATE

A ride-sharing web app built with Flask. Users can post rides, request to join others' rides, chat in real time, rate each other, and manage their travel — while admins moderate users and reported rides.

## Features

### Accounts & Profiles
- **Registration with email verification** — new users receive a confirmation email (token valid for 1 hour) before their account is verified.
- **Secure login/logout** — passwords hashed with Werkzeug; sessions managed by Flask-Login.
- **Profile management** — name, phone, address, gender, NID, blood group, preferred travel mode, profile picture, and ID document uploads.
- **Travel preferences** — home location, frequent routes, and safety preferences used to personalize recommendations.
- **Ratings & reputation** — users earn an average rating from feedback left on their rides.

### Rides
- **Create ride posts** — origin/destination (with map coordinates), date, time, available seats, fare type, estimated cost, description, gender preference, and an option to require verified users only.
- **Edit / delete** your own ride posts.
- **Smart ride feed** — rides are filtered (by location, fare type, date, today-or-later) and ranked by a match score based on your home location, frequent routes, preferred fare, gender preference, verification status, proximity in days, and the poster's rating.
- **Request to join rides** — with duplicate-request prevention and seat tracking.
- **Accept / reject requests** — ride owners manage incoming requests; seats decrement on acceptance.
- **Manually add riders** ("sharable people") — owners can add or remove specific users to a ride.
- **Dashboard** — upcoming rides, your ride requests, travel history, and recommended rides.
- **Past journeys** — full travel history.
- **Feedback & ratings** — leave a comment and rating on rides, updating the owner's reputation.

### Communication
- **Real-time chat** — one-to-one messaging powered by Flask-SocketIO, with rooms per chat.
- **Unread message tracking** — unread counts surfaced across the app.
- **Notifications** — for ride requests, acceptances/rejections, admin actions, and reports, with read/unread state and click-through links.

### Admin
- **Admin login** (separate from user auth, session-based).
- **Admin dashboard** — counts of users, rides, feedback, and deleted rides.
- **User management** — verify, approve, restrict, or delete users.
- **Add / remove admins.**
- **Reported rides** — users can report rides; admins review and delete them.
- **Soft-delete audit trail** — admin-deleted rides are archived in `DeletedRide`, and all affected parties are notified.

## Tech Stack

- **Backend:** Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Flask-Mail, Flask-SocketIO
- **Database:** MySQL (via PyMySQL) — configurable through `SQLALCHEMY_DATABASE_URI`
- **Frontend:** Jinja2 templates, Bootstrap-Flask
- **Config:** environment variables loaded via `python-dotenv`

## Prerequisites

- Python 3.11+
- A MySQL database (the default config points at a hosted Railway instance)
- SMTP credentials for sending verification emails (e.g. a Gmail app password)

## Setup

1. **Clone and enter the project**
   ```bash
   cd "UNI TRAVEL MATE"
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # Windows (PowerShell)
   venv\Scripts\Activate.ps1
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables** — create a `.env` file in the project root:
   ```env
   SQLALCHEMY_DATABASE_URI=mysql+pymysql://USER:PASSWORD@HOST:PORT/DBNAME
   SQLALCHEMY_TRACK_MODIFICATIONS=False

   SECRET_KEY=change-this-to-a-random-secret

   # Email (SMTP)
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=you@example.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER_NAME=ride share
   MAIL_DEFAULT_SENDER_EMAIL=you@example.com
   ```
   `config.py` reads these values and exposes them to the app. The `.env` file is git-ignored.

5. **Create the database tables**
   ```bash
   python createdb.py
   ```

6. **(Optional) Create an admin account**
   ```bash
   python create.py
   ```
   This creates an admin with email `admin@example.com` and password `admin123` — change these in `create.py` (or via the admin panel) before any real use.

## Running the App

```bash
python app.py
```

The app starts via SocketIO (required for real-time chat) on `http://127.0.0.1:5000/` in debug mode.

- User site: `http://127.0.0.1:5000/`
- Admin login: `http://127.0.0.1:5000/admin/login`

## Database Migrations

The project is set up with Flask-Migrate. To apply schema changes:

```bash
flask db migrate -m "describe change"
flask db upgrade
```

## Project Structure

```
UNI TRAVEL MATE/
├── app.py            # Main application: routes, auth, rides, chat, admin
├── config.py         # Loads configuration from environment (.env)
├── models.py         # SQLAlchemy models (User, RidePost, Chat, etc.)
├── createdb.py       # Creates all database tables
├── create.py         # Seeds an initial admin account
├── requirements.txt  # Python dependencies
├── migrations/       # Flask-Migrate migration scripts
├── templates/        # Jinja2 HTML templates
└── static/           # CSS, JS, and uploaded profile pictures / documents
```

## Notes

- Uploaded profile pictures and ID documents are stored under `static/profile_pics/`.
- Email verification is required for sensitive actions like creating rides and leaving feedback.
- Keep `SECRET_KEY` and mail/database credentials out of version control — use the `.env` file.
