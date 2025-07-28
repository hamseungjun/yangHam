import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

# .env 파일에서 환경 변수를 로드합니다 (로컬 개발용)
load_dotenv()

# os.getenv를 사용해 환경 변수를 직접 읽어옵니다.
DATABASE_URL = os.getenv("DATABASE_URL")

# Render에서 제공하는 postgresql:// URL을 비동기용 postgresql+psycopg_async:// 로 변경
if DATABASE_URL and DATABASE_URL.startswith("postgresql://"):
    DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg_async://", 1)

engine = create_async_engine(DATABASE_URL) if DATABASE_URL else None
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine) if engine else None
Base = declarative_base()

async def get_db():
    if SessionLocal is None:
        raise Exception("Database session could not be established.")
    async with SessionLocal() as session:
        yield session