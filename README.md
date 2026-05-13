# Trading Journal — Flask Web Application

## Overview

Tradefy is a web application built with Flask that helps traders track, review, and analyze their trades in one place. 
The application includes secure authentication, trade logging, performance tracking, and dashboard analytics to help users improve trading discipline and decision-making.

## Testing
For testing, keep "TESTING" and "MAIL_SUPRESS_SEND" as "True" in config.py, else "False".

---

## Features

- User authentication and account management
- Secure password hashing with Flask-Bcrypt
- Login session management with Flask-Login
- Trade entry and trade history tracking
- Dashboard analytics and statistics
- Form validation with WTForms
- Email support password resets
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

### Additional Libraries
- NumPy
- itsdangerous

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/picklesin/flask-stock-trading-journal.git
cd trading-journal
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows
```bash
venv\Scripts\activate
```

#### macOS/Linux
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
flask db init migrate
flask db upgrade
```

### 5. Start the Application

```bash
flask run
```

---


## Security Features

- Password hashing with Flask-Bcrypt
- Session authentication
- CSRF protection with Flask-WTF
- Secure token generation with itsdangerous

---

## Future Improvements

- Trade performance charts
- CSV import/export
- Risk management metrics
- Advanced filtering and search
- Mobile optimization
- Broker API integration

---
