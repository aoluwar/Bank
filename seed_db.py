import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from models import Base, Customer
from sample_customers import nigerian_customers

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/postgres"
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def seed():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with SessionLocal() as session:
        for cust in nigerian_customers:
            exists = await session.execute(
                Customer.__table__.select().where(Customer.email == cust["email"])
            )
            if not exists.first():
                session.add(Customer(**cust))
        await session.commit()
    print("Seeded 1,000 Nigerian customers.")

if __name__ == "__main__":
    asyncio.run(seed())