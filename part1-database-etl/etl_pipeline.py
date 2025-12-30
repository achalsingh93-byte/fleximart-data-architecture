import pandas as pd
import pymysql
import re
from datetime import datetime

# ---------------- DATABASE CONFIG ----------------
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "Success@93"   # <-- apna MySQL password yahan daalna
DB_NAME = "fleximart"

# ---------------- HELPER FUNCTIONS ----------------
def normalize_phone(phone):
    if pd.isna(phone):
        return None
    digits = re.sub(r"\D", "", str(phone))
    return digits[-10:] if len(digits) >= 10 else None

def parse_date(value):
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%d-%m-%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except:
            continue
    return None

# ---------------- MAIN ETL FUNCTION ----------------
def main():

    # EXTRACT
    customers = pd.read_csv("data/customers_raw.csv")
    products = pd.read_csv("data/products_raw.csv")
    sales = pd.read_csv("data/sales_raw.csv")

    # TRANSFORM - CUSTOMERS
    customers = customers.drop_duplicates(subset=["customer_id"])
    customers["email"] = customers["email"].fillna(
        customers["first_name"].str.lower() + "." +
        customers["last_name"].str.lower() + "@fleximart.com"
    )
    customers["phone"] = customers["phone"].apply(normalize_phone)
    customers["city"] = customers["city"].str.title()
    customers["registration_date"] = customers["registration_date"].astype(str).apply(parse_date)

    # TRANSFORM - PRODUCTS
    products["product_name"] = products["product_name"].str.strip()
    products["category"] = products["category"].str.title()
    products["price"] = pd.to_numeric(products["price"], errors="coerce")
    products["price"] = products.groupby("category")["price"].transform(lambda x: x.fillna(x.median()))
    products["stock_quantity"] = pd.to_numeric(products["stock_quantity"], errors="coerce").fillna(0)

    # TRANSFORM - SALES
    sales = sales.drop_duplicates(subset=["transaction_id"])
    sales = sales.dropna(subset=["customer_id", "product_id"])
    sales = sales[sales["status"] == "Completed"]
    sales["transaction_date"] = sales["transaction_date"].astype(str).apply(parse_date)

    # LOAD
    conn = pymysql.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME,
    ssl_disabled=True
)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        customer_id INT PRIMARY KEY AUTO_INCREMENT,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(100) UNIQUE,
        phone VARCHAR(20),
        city VARCHAR(50),
        registration_date DATE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        product_id INT PRIMARY KEY AUTO_INCREMENT,
        product_name VARCHAR(100),
        category VARCHAR(50),
        price DECIMAL(10,2),
        stock_quantity INT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INT PRIMARY KEY AUTO_INCREMENT,
        customer_id INT,
        order_date DATE,
        total_amount DECIMAL(10,2),
        status VARCHAR(20),
        FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS order_items (
        order_item_id INT PRIMARY KEY AUTO_INCREMENT,
        order_id INT,
        product_id INT,
        quantity INT,
        unit_price DECIMAL(10,2),
        subtotal DECIMAL(10,2),
        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    )
    """)

    conn.commit()
    conn.close()

    print("ETL pipeline file created successfully")

if __name__ == "__main__":
    main()
