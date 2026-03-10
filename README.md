# Expense Tracker API — Flask Implementation
Expense Tracker REST API built with Flask

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
│   ├── routes
│   ├── models
│   ├── controllers
│   ├── utils
│   └── __init__.py
│
├── config.py
├── run.py
├── requirements.txt
└── README.md
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
