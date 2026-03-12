from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

"""Initialize the database tables manually.

Usage:
  python backend/scripts/init_db.py

It uses DATABASE_URL if set, otherwise creates ./tasks.db (SQLite).
"""

from app.database import Base, engine
from app import models  # noqa: F401 - import models so metadata includes tables


def main() -> None:
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully.")
    print(f"Engine URL: {engine.url}")


if __name__ == "__main__":
    main()
