"""Check DB connection and list tables.

Run: python check_db.py
"""
import sys
from sqlalchemy import inspect
from config.config import engine

expected = ["usuarios", "equipes", "atletas", "presencas", "videos"]

def main():
    try:
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        print("Found tables:", tables)
        missing = [t for t in expected if t not in tables]
        if missing:
            print("Missing tables:", missing)
            sys.exit(2)
        else:
            print("All expected tables are present.")
            sys.exit(0)
    except Exception as e:
        print("Error connecting or inspecting the database:", e)
        sys.exit(1)

if __name__ == '__main__':
    main()
