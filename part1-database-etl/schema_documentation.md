# Schema Documentation – FlexiMart Database

## Overview
This document describes the relational database schema designed for **Part 1: Database ETL** of the FlexiMart Data Architecture assignment.  
The schema supports customer management, product cataloging, and order transactions required for downstream analytics.

Database Name: **fleximart**  
Database Engine: **MySQL**

---

## Entity Relationship Summary

The database consists of the following core entities:

- **customers** → Stores customer master data  
- **products** → Stores product catalog information  
- **orders** → Stores order header information  
- **order_items** → Stores line-level order details  

Relationships:
- One customer can place multiple orders  
- One order can contain multiple products  
- Products can appear in multiple orders  

---

## Table Definitions

---

### 1. customers

Stores customer master information.

| Column Name       | Data Type     | Constraints                        | Description |
|------------------|--------------|------------------------------------|------------|
| customer_id      | INT          | PRIMARY KEY, AUTO_INCREMENT        | Unique customer identifier |
| first_name       | VARCHAR(50)  | NOT NULL                           | Customer first name |
| last_name        | VARCHAR(50)  | NOT NULL                           | Customer last name |
| email            | VARCHAR(100) | UNIQUE, NOT NULL                   | Customer email address |
| phone            | VARCHAR(15)  | NULL                               | Normalized phone number |
| city             | VARCHAR(50)  | NULL                               | Customer city |
| registration_date| DATE         | NOT NULL                           | Customer registration date |

Purpose:  
Used as the primary customer dimension for order analytics.

---

### 2. products

Stores product catalog information.

| Column Name | Data Type     | Constraints                        | Description |
|------------|--------------|------------------------------------|------------|
| product_id| INT          | PRIMARY KEY, AUTO_INCREMENT        | Unique product identifier |
| name       | VARCHAR(100) | NOT NULL                           | Product name |
| category   | VARCHAR(50)  | NOT NULL                           | Product category |
| price      | DECIMAL(10,2)| NOT NULL                           | Product price |
| stock_qty | INT          | NOT NULL                           | Available stock quantity |

Purpose:  
Supports product-level analytics such as category-wise pricing and inventory tracking.

---

### 3. orders

Stores order-level transactional data.

| Column Name | Data Type | Constraints                 | Description |
|------------|----------|-----------------------------|------------|
| order_id   | INT      | PRIMARY KEY, AUTO_INCREMENT | Unique order identifier |
| customer_id| INT      | FOREIGN KEY (customers)     | Customer placing the order |
| order_date | DATE     | NOT NULL                    | Order date |

Foreign Key:
- customer_id → customers(customer_id)

Purpose:  
Acts as the order header table linking customers to purchased items.

---

### 4. order_items

Stores line-level details of each order.

| Column Name | Data Type | Constraints                 | Description |
|------------|----------|-----------------------------|------------|
| item_id    | INT      | PRIMARY KEY, AUTO_INCREMENT | Unique line item ID |
| order_id   | INT      | FOREIGN KEY (orders)        | Associated order |
| product_id | INT      | FOREIGN KEY (products)      | Purchased product |
| quantity   | INT      | NOT NULL                    | Quantity ordered |
| price      | DECIMAL(10,2)| NOT NULL                 | Price at time of purchase |

Foreign Keys:
- order_id → orders(order_id)  
- product_id → products(product_id)

Purpose:  
Enables revenue calculations, product-level sales analysis, and order composition analysis.

---

## Data Integrity & Constraints

- Primary keys ensure entity uniqueness
- Foreign keys enforce referential integrity
- Email field in customers table is unique to avoid duplicate customer records
- Price and quantity fields are non-null to ensure accurate financial calculations

---

## Design Considerations

- Schema follows **3rd Normal Form (3NF)**
- Separation of order headers and order items allows scalable transaction modeling
- Designed to support downstream warehouse modeling (facts and dimensions)

---

## Analytics Readiness

This schema supports:
- Customer order frequency analysis
- Product category performance
- Average pricing by category
- Order volume per customer
- Foundation for star-schema transformation in Part 3

---

## Conclusion

The FlexiMart relational schema is optimized for transactional integrity, analytical flexibility, and seamless integration with ETL pipelines and downstream data warehouse layers.
