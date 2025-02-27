import sqlite3


class Database:
    def __init__(self, path):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reviews(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    instagram_username TEXT,
                    rate INTEGER,
                    extra_comments TEXT
                )        
            """),
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS store(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_product TEXT,
                    size TEXT,
                    category TEXT,
                    price INTEGER,
                    photo TEXT,
                    product_id INTEGER

                )
            """),
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS products_details(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    category TEXT,
                    infoproduct TEXT
                )
             """)
            conn.commit()
    def add_complaint(self, data: dict):
        print(data)
        with sqlite3.connect(self.path) as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO reviews (name, instagram_username, rate ,extra_comments) VALUES (?, ?, ?, ?)
            """,
                (data["name"],data["instagram_username"] ,data["rate"], data["extra_comments"]),
            )
            conn.commit()