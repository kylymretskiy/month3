CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_product TEXT,
                    size TEXT,
                    category TEXT,products_details
                    price INTEGER,
                    photo TEXT,
                    product_id INTEGER
                )
"""

CREATE_TABLE_products_details = """
    CREATE TABLE IF NOT EXISTS products_details(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    category TEXT,
                    infoproduct TEXT
                )
"""

CREATE_TABLE_collection_products = """
    CREATE TABLE IF NOT EXISTS collection_products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    product_id INTEGER,
                    collection TEXT
                )
"""

INSERT_store_query = """
    INSERT INTO store (name_product,category, price, size ,product_id,photo) 
    VALUES (?, ?, ?, ?,?,?)
"""
INSERT_products_details_query = """
INSERT INTO products_details (category, product_id) 
    VALUES (?, ?)
"""
INSERT_collection_products_query = """
INSERT INTO collection_products (product_id,collection ) 
    VALUES (?, ?)
"""