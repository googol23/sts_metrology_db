# project_root/db.py
import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import Base

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DATABASE_PATH = Path(os.getenv("METROLOGY_DB_PATH", PACKAGE_ROOT / "data" / "metrology.db"))
DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)
engine = create_engine(f"sqlite:///{DATABASE_PATH}", echo=True)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)