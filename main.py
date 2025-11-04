import uuid
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import models
import crud
from schemas import *

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@db:5432/postgres"
engine = create_async_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

app = FastAPI(
    title="Bank REST API with Docker & PostgreSQL",
    description="Scalable bank backend with FastAPI, SQLAlchemy, and Docker.",
    version="2.0.0",
)

async def get_db():
    async with SessionLocal() as session:
        yield session

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.post("/customers", response_model=CustomerInfo)
async def create_customer(data: CustomerCreate, db: AsyncSession = Depends(get_db)):
    customer = await crud.create_customer(db, data.name)
    account_ids = [acc.id for acc in customer.accounts]
    return CustomerInfo(id=customer.id, name=customer.name, accounts=account_ids)

@app.get("/customers", response_model=list[CustomerInfo])
async def list_customers(db: AsyncSession = Depends(get_db)):
    customers = await crud.get_customers(db)
    return [CustomerInfo(id=c.id, name=c.name, accounts=[acc.id for acc in c.accounts]) for c in customers]

@app.post("/accounts", response_model=AccountInfo)
async def open_account(data: AccountCreate, db: AsyncSession = Depends(get_db)):
    account = await crud.create_account(db, data.customer_id, data.initial_balance)
    return AccountInfo(id=account.id, owner_id=account.owner_id, balance=account.balance, transactions=[txn.id for txn in account.transactions])

@app.get("/accounts/{account_id}", response_model=AccountInfo)
async def get_account(account_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    account = await crud.get_account(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return AccountInfo(id=account.id, owner_id=account.owner_id, balance=account.balance, transactions=[txn.id for txn in account.transactions])

@app.post("/transaction", response_model=TransactionInfo)
async def make_transaction(data: TransactionCreate, db: AsyncSession = Depends(get_db)):
    try:
        txn = await crud.create_transaction(db, data.account_id, data.amount, data.type)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not txn:
        raise HTTPException(status_code=404, detail="Account not found")
    return TransactionInfo(id=txn.id, account_id=txn.account_id, amount=txn.amount, type=txn.type)

@app.get("/accounts/{account_id}/transactions", response_model=list[TransactionInfo])
async def get_transactions(account_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    txns = await crud.get_account_transactions(db, account_id)
    return [TransactionInfo(id=txn.id, account_id=txn.account_id, amount=txn.amount, type=txn.type) for txn in txns]