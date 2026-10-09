# Expense Tracker API

A REST API built with **FastAPI** where users register, log in with **JWT authentication**, and manage their own expenses (full CRUD). Each user can see and change only their own expenses.

## Project concept

The main resource is **expenses**:

| Field | Description |
|---|---|
| id | Auto-generated unique id |
| title | Short name, e.g. "Lunch" |
| amount | Amount spent (must be greater than 0) |
| category | e.g. Food, Travel |
| description | Optional note |
| expense_date | Date of the expense (defaults to today) |
| created_at | Auto timestamp |
| owner_id | The user who owns the expense (set from the token) |

## Tech stack

Python 3.10+, FastAPI, Uvicorn, Pydantic, SQLAlchemy, SQLite, PyJWT, passlib (bcrypt)

## Project structure

```
expense-tracker-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── auth.py
│   └── routers/
│       ├── __init__.py
│       ├── auth.py
│       └── expenses.py
├── screenshots/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup

1. Clone the repository

```bash
git clone https://github.com/janani40/Expense-tracker-api.git
cd Expense-tracker-api
```

2. Create and activate a virtual environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create the `.env` file from the example

```bash
# Windows
copy .env.example .env
# Mac/Linux
cp .env.example .env
```

Then open `.env` and replace the `SECRET_KEY` value with your own. Generate one with:

```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

5. Run the server

```bash
uvicorn app.main:app --reload
```

6. Open Swagger docs at http://127.0.0.1:8000/docs

The database file (`expenses.db`) and tables are created automatically on first run.

## Environment variables

| Variable | Description | Example |
|---|---|---|
| SECRET_KEY | Secret used to sign JWT tokens | a long random string |
| ALGORITHM | JWT signing algorithm | HS256 |
| ACCESS_TOKEN_EXPIRE_MINUTES | Token lifetime in minutes | 30 |
| DATABASE_URL | Database connection string | sqlite:///./expenses.db |

## API endpoints

| Method | Route | Auth | Purpose | Status codes |
|---|---|---|---|---|
| POST | /auth/register | No | Create a new user | 201, 409 if user exists, 422 |
| POST | /auth/login | No | Get a JWT access token | 200, 401 |
| GET | /auth/me | Yes | Get the current user | 200, 401 |
| POST | /expenses | Yes | Create an expense | 201, 422 |
| GET | /expenses | Yes | List your expenses (`skip`, `limit`) | 200 |
| GET | /expenses/{id} | Yes | Get one expense | 200, 404 |
| PUT | /expenses/{id} | Yes | Update an expense | 200, 404, 422 |
| DELETE | /expenses/{id} | Yes | Delete an expense | 204, 404 |

## How to use (Swagger)

1. Open `/docs` and call **POST /auth/register** to create a user.
2. Click **Authorize**, enter your username (or email) and password.
3. All protected routes now work with your token automatically.

## Security notes

- Passwords are hashed with bcrypt, never stored as plain text.
- JWT tokens expire after the time set in `.env`.
- Secrets live in `.env`, which is not committed.
- A user can only access their own expenses. Another user's record returns 404.

## Screenshots

Swagger test screenshots are in the [`screenshots/`](screenshots/) folder: register, duplicate user, login, all CRUD methods, validation error, unauthorized access and ownership tests.