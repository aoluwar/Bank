
# 🏦 Bank REST API (FastAPI + SQLAlchemy + Docker)

A scalable bank backend using FastAPI, SQLAlchemy with PostgreSQL, Docker, and docker-compose.

## Features

- Customer management (100+ customers supported)
- Account management
- Deposits & withdrawals with transaction history
- Persistent PostgreSQL storage
- Docker-based deployment
- RESTful API with Swagger docs

## Setup & Usage

### 1. Build & start with Docker Compose

```bash
docker-compose up --build
```

- Backend: http://localhost:8000
- Docs: http://localhost:8000/docs

### 2. API Endpoints

- `POST /customers` — Create customer
- `GET /customers` — List customers
- `POST /accounts` — Open account
- `GET /accounts/{account_id}` — Account details
- `POST /transaction` — Deposit/Withdraw
- `GET /accounts/{account_id}/transactions` — Transaction history

### 3. Database

- Default DB is PostgreSQL (see `docker-compose.yml`)
- DB user/password: `postgres`
- Change `DATABASE_URL` in code/Docker as needed

### 4. Database Schema/Migrations

Uses SQLAlchemy for schema, recommends Alembic for upgrades:

```bash
alembic init alembic
# Edit alembic/env.py for database URL
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### 5. Extending

- Add authentication, user roles, account transfers, pagination, etc.

---

**MIT License**
## Alembic Migration

1. Install Alembic:
    ```
    pip install alembic
    alembic init alembic
    ```
2. Edit `alembic/env.py` for DB connection:
    ```
    config.set_main_option('sqlalchemy.url', 'postgresql+psycopg2://postgres:postgres@localhost:5432/postgres')
    ```
3. Run migration:
    ```
    alembic revision --autogenerate -m "Initial migration"
    alembic upgrade head
    ```

## Seed Demo Data
To seed your DB with 1,000 entries:
```bash
python seed_db.py
```

## Frontend Integration

Use the sample React UI in `src/components/CustomerList.js` to list customers.  
API endpoints: `/customers`

---

