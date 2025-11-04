from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound
from models import Customer, Account, Transaction

async def create_customer(db: AsyncSession, name: str):
    customer = Customer(name=name)
    db.add(customer)
    await db.commit()
    await db.refresh(customer)
    return customer

async def get_customers(db: AsyncSession):
    result = await db.execute(select(Customer))
    return result.scalars().all()

async def create_account(db: AsyncSession, owner_id, initial_balance):
    account = Account(owner_id=owner_id, balance=initial_balance)
    db.add(account)
    await db.commit()
    await db.refresh(account)
    return account

async def get_account(db: AsyncSession, account_id):
    result = await db.execute(select(Account).where(Account.id == account_id))
    account = result.scalar_one_or_none()
    return account

async def create_transaction(db: AsyncSession, account_id, amount, type_):
    account = await get_account(db, account_id)
    if not account:
        return None
    if type_ == "withdraw" and account.balance < amount:
        raise ValueError("Insufficient funds")
    if type_ == "deposit":
        account.balance += amount
    elif type_ == "withdraw":
        account.balance -= amount
    txn = Transaction(account_id=account_id, amount=amount, type=type_)
    db.add(txn)
    await db.commit()
    await db.refresh(txn)
    return txn

async def get_account_transactions(db: AsyncSession, account_id):
    result = await db.execute(select(Transaction).where(Transaction.account_id == account_id))
    return result.scalars().all()