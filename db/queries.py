CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_product TEXT,
                    size TEXT
                    category TEXT,
                    price INTEGER,
                    photo TEXT,
                    product_id INTEGER
                )
"""

CREATE_TABLE_details = """
    CREATE TABLE IF NOT EXISTS products_details(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    category TEXT,
                    infoproduct TEXT
                )
"""

INSERT_STORE_querry = """
    INSERT INTO store (name_product, price, size ,product_id,photo) 
    VALUES (?, ?, ?, ?,?)
"""
INSERT_STORE_DETAILS_querry = """
INSERT INTO store (category, product_id) 
    VALUES (?, ?)
"""
