# Expense Tracker API — Flask Implementation
Expense Tracker REST API built with Flask  
Progress:   
Phase 1 — Flask App Architecture [Done]  
Phase 2 — Configuration & Environment Variables [Done]  
Phase 3 — Database Connection [Done]  
Phase 4 — Database Schema [Done]  
Phase 5 — User Authentication  
Phase 6 — JWT Middleware  
Phase 7 — Expense CRUD API  
Phase 8 — Filtering & Query Features  

## Project Goals
- Compare backend architecture between Express.js and Flask by implementing the same system in both frameworks.
- Practice **backend API design** using Flask
- Apply **relational database concepts** (schema design, constraints, queries)

This project follows the idea from  
[JordznFish – Expense Tracker API (Node.js)](https://github.com/JordznFish/Expenses-tracker-API)  

---

## Features

### Authentication
- User registration and login
- JWT-based authentication
- Protected routes for user data

### Expense Management
- Create, read, update, delete expenses
- Each expense includes:
  - Amount
  - Category
  - Description
  - Date
- Expenses are scoped per user

### Filtering & Queries
- Filter expenses by:
  - Date range
  - Category
- Basic pagination for large datasets

---

## Tech Stack

| Layer | Technology |
|------|-----------|
| Runtime | Python |
| Backend Framework | Flask |
| Language | Python |
| Database | PostgreSQL |
| Database Access | Raw SQL (psycopg2) |
| Authentication | JSON Web Tokens (JWT) |
| API Testing | Postman |
| Version Control | Git |

---

## Project Structure

```
expense-tracker-flask
│
├── app
│   │
│   ├── __init__.py
│   │
│   ├── routes
│   │   ├── auth_routes.py
│   │   └── expense_routes.py
│   │
│   ├── controllers
│   │   ├── auth_controller.py
│   │   └── expense_controller.py
│   │
│   ├── models
│   │   ├── user_model.py
│   │   ├── category_model.py
│   │   └── expense_model.py
│   │
│   └── utils
│       ├── db.py
│       ├── jwt_handler.py
│       └── password_utils.py
│
├── config.py
├── run.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md

Supplementary knowledge:
We're using MVC (Model-View-Controller) Architecture.
End User -> End point -> Controllers -> Model -> Controllers -> View 

__init__.py: When we run app package, this file will always be executed initially. Mainly returning 'app' object
routes folder: Where we define the routing logic (Using Blueprint class from Flask Package)
controllers: Where all the APIs logic live, we handle the req and res operations.
models: A folder to communicate with tables from our Database, a connection between backend and database
utils: A utility folder that handles some useful logic or functions such as jwt or bcryting password.
config.py: A file to load and store variables in a class from .env, so we could retrieve env variables (Personal infos)
run.py: Where we execute our website (python run.py)
requirements.txt: Others could run pip -r requirement to install dependencies
.env: Personal Infos
.env.example: Template of .env
```

---

## Database Design (Overview)

Core tables:

### `users`

- id (PK)
- email
- password_hash
- created_at

### `categories`

- id (PK)
- name

### `expenses`

- id (PK)
- user_id
- category_id
- amount
- description
- expense_date
- created_at

Key concepts applied:

- Primary keys (PK)
- Foreign key relationships (FK)
- NOT NULL and CHECK constraints
- Indexed columns for query performance

---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|------|---------|------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive JWT |

---

### Expenses

| Method | Endpoint | Description |
|------|---------|------------|
| GET | `/expenses` | Get all expenses for logged-in user |
| POST | `/expenses` | Create a new expense |
| PUT | `/expenses/<id>` | Update an expense |
| DELETE | `/expenses/<id>` | Delete an expense |

---

## Environment Variables

Create a `.env` file based on `.env.example`:

```
PORT=5000
DATABASE_URL=postgresql://user:password@localhost:5432/expense_tracker
JWT_SECRET=your_jwt_secret
```

---

## Setup & Run

### 1. Create virtual environment

```bash
python -m venv venv
```

### 2. Activate environment

Windows

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
python run.py
```

The API will be available at:

```
http://localhost:5000
```

---

## Future Improvements

- Expense analytics and monthly reports
- Category management API
- Role-based authorization
- Docker containerization
- Frontend client integration

---
