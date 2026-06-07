import sqlite3
from typing import List, Tuple, Any


class DBClient:
    def __init__(self, db_path: str = "test_data.db"):
        self.db_path = db_path

    def connect(self):
        return sqlite3.connect(self.db_path)

    def fetch_all(self, query: str, params: Tuple = ()) -> List[Any]:
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()
        conn.close()
        return rows

    def fetch_one(self, query: str, params: Tuple = ()) -> Any:
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        row = cursor.fetchone()
        conn.close()
        return row

    def execute(self, query: str, params: Tuple = ()) -> None:
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        conn.close()