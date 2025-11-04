from pydantic import BaseModel, Field, EmailStr
from typing import List
import uuid
from datetime import datetime

class CustomerCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str | None = None

class CustomerInfo(BaseModel):
    id: uuid.UUID
    name: str
    email: EmailStr
    phone: str | None = None
    created_at: datetime
    accounts: List[uuid.UUID] = []

class AccountCreate(BaseModel):
    customer_id: uuid.UUID
    initial_balance: float = Field(ge=0, default=0)

class AccountInfo(BaseModel):
    id: uuid.UUID
    owner_id: uuid.UUID
    balance: float
    created_at: datetime
    transactions: List[uuid.UUID] = []

class TransactionCreate(BaseModel):
    account_id: uuid.UUID
    amount: float = Field(gt=0)
    type: str  # 'deposit' or 'withdraw'

class TransactionInfo(BaseModel):
    id: uuid.UUID
    account_id: uuid.UUID
    amount: float
    type: str
    created_at: datetime