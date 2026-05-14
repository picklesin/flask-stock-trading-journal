---

# Trading Journal — Flask Web Application

## Overview

This trading journal is a web application built with Flask that helps traders track, review, and analyze their trades in one place.
The application includes secure authentication, trade logging, performance tracking, and an interactive dashboard to help users improve trading discipline and decision-making.

---

## Features

- User authentication and account management
- Secure password hashing with Flask-Bcrypt
- Login session management with Flask-Login
- Trade entry and trade history tracking
- Interactive dashboard with cumulative P&L, win rate, and avg win/loss charts
- Form validation with WTForms
- Email support for password resets
- Database integration with SQLAlchemy
- Database migrations using Flask-Migrate
- Responsive Flask templates

---

## Tech Stack

### Backend

- Python
- Flask
- SQLAlchemy
- Flask-Login
- Flask-WTF
- Flask-Bcrypt
- Flask-Migrate
- Flask-Mail

### Database

- SQLite

### Frontend

- HTML
- CSS
- Jinja2 Templates
- Chart.js

### Additional Libraries

- NumPy
- itsdangerous

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/picklesin/flask-stock-trading-journal.git
cd flask-stock-trading-journal
```

### 2. Create a Virtual Environment

```
python -m venv venv
```

Activate the environment:

#### Windows

```
venv\Scripts\activate
```

#### macOS/Linux

```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run Database Migrations

```
flask db upgrade
```

### 5. Start the Application

```
flask run
```

> **Note:** For testing, set `TESTING = True` and `MAIL_SUPPRESS_SEND = True` in `config.py`.

---

## Security Features

- Password hashing with Flask-Bcrypt
- Session authentication
- CSRF protection with Flask-WTF
- Secure token generation with itsdangerous

---

## Future Improvements

- CSV import/export
- Risk management metrics (R-multiple, max drawdown)
- Advanced filtering and search
- Mobile optimization
- Broker API integration

---

