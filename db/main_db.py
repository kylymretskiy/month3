import sqlite3
from db import queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def create_tables():
    if db:
        print('База данных подключена!')

    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_products_details)
    cursor.execute(queries.CREATE_TABLE_collection_products)


async def sql_insert_store(name_product,category, price, size, product_id, photo):
    cursor.execute(queries.INSERT_store_query,
                   (name_product,category, price, size, product_id, photo))
    db.commit()


async def sql_insert_collection_products( product_id, collection):
    cursor.execute(queries.INSERT_collection_products_query,
                   ( product_id, collection))
    db.commit()

async def sql_insert_products_details(category, product_id):
    cursor.execute(queries.INSERT_products_details_query,
                   (category, product_id))
    db.commit()

# ==========================================================

def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    select * from store s
    INNER JOIN products_details pd on s.product_id=pd.product_id
    INNER JOIN collection_products cp ON s.product_id = cp.product_id;
    """).fetchall()
    conn.close()
    return products

def update_product_field(product_id, field_name, new_value):
    conn = get_db_connection()

    store_table = ['name_product', 'category', 'price', 'size', 'product_id', 'photo']
    products_details_table = ['category', 'product_id']
    store_collection_products_table = ['product_id', 'collection']

    try:
        if field_name in store_table:
            query = f'UPDATE store SET {field_name} = ? WHERE product_id = ?'
        elif field_name in products_details_table:
            query = f'UPDATE products_details SET {field_name} = ? WHERE product_id = ?'

        elif field_name in store_collection_products_table:
            query = f'UPDATE collection_products SET {field_name} = ? WHERE product_id = ?'

        else:
            raise ValueError(f'Нет такого поля как {field_name}')

        conn.execute(query, (new_value, product_id))
        conn.commit()

    except sqlite3.OperationalError as error:
        print(f'Ошибка - {error}')

    finally:
        conn.close()