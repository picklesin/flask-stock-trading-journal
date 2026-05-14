Flask Trading Journal
A full-stack web application for traders to log, review, and analyze their trades in one place.
Overview
Tradefy helps traders build discipline and improve performance by tracking trade history and visualizing key metrics — including cumulative P&L, win rate, and average win vs. loss — through an interactive dashboard.
Features

User authentication and account management
Secure password hashing with Flask-Bcrypt
Login session management with Flask-Login
Trade entry and trade history tracking
Interactive dashboard with cumulative P&L, win rate, and avg win/loss charts
Form validation with WTForms
Password reset via email
Database integration with SQLAlchemy
Database migrations with Flask-Migrate
CSRF protection with Flask-WTF

Tech Stack
Backend: Python, Flask, SQLAlchemy, Flask-Login, Flask-WTF, Flask-Bcrypt, Flask-Migrate, Flask-Mail
Frontend: HTML, CSS, Jinja2, Chart.js
Database: SQLite
Installation

Clone the repo and navigate into it:

git clone https://github.com/picklesin/flask-stock-trading-journal.git
cd flask-stock-trading-journal

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Run database migrations:

flask db upgrade

Start the app:

flask run

Note: For testing, set TESTING = True and MAIL_SUPPRESS_SEND = True in config.py.

Future Improvements

CSV import/export
Risk management metrics (R-multiple, max drawdown)
Advanced filtering and search
Mobile optimization
Broker API integration
