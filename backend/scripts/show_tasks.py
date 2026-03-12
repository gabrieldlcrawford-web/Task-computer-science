from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

"""Print tasks directly from the configured database.

Usage:
  python backend/scripts/show_tasks.py
"""

from sqlalchemy import select

from app.database import SessionLocal
from app.models import Task


def main() -> None:
    with SessionLocal() as db:
        rows = db.execute(select(Task).order_by(Task.created_at.desc())).scalars().all()

    if not rows:
        print("No tasks found.")
        return

    for task in rows:
        status = "DONE" if task.done else "TODO"
        print(f"[{status}] #{task.id} {task.title}")
        if task.description:
            print(f"  - {task.description}")


if __name__ == "__main__":
    main()
