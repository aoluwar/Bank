from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sample_customers import nigerian_customers
from crud import create_customer

router = APIRouter()

@router.post("/seed_customers")
async def seed_customers(db: AsyncSession = Depends(get_db)):
    for cust in nigerian_customers:
        await create_customer(db, cust["name"], cust["email"], cust["phone"])
    return {"status": "Seeded Nigerian customers"}