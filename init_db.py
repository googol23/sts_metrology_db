# init_db.py
import os
from pathlib import Path

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker

from .models import Base

# --- 1. Create SQLite database ---
PACKAGE_ROOT = Path(__file__).resolve().parent
DATABASE_PATH = Path(os.getenv("METROLOGY_DB_PATH", PACKAGE_ROOT / "data" / "metrology.db"))
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True shows SQL statements

# --- 2) Create all tables ---
Base.metadata.create_all(engine)

# --- 3) Print all tables ---
inspector = inspect(engine)
tables = inspector.get_table_names()
print("Tables created in database:")
for table in tables:
    print(f"- {table}")

# --- 4) Optional: create a session to test ---
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()
print("Session created successfully:", session)
session.close()