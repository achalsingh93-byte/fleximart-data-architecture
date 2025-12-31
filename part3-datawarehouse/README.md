
# Part 3: Data Warehouse

This section will contain data warehouse schema, fact & dimension tables, and analytical queries.

# Part 3: Data Warehouse and Analytics – FlexiMart

## Overview
This part implements a dimensional data warehouse for FlexiMart to analyze historical sales patterns. A star schema is designed and populated with realistic sample data, followed by OLAP-style analytical queries to support business decision-making.

The data warehouse enables time-based analysis, product performance evaluation, and customer segmentation using fact and dimension tables.

---

## Components Implemented

### 1. Star Schema Design
Documented in `star_schema_design.md`, covering:
- Fact table: `fact_sales`
- Dimension tables: `dim_date`, `dim_product`, `dim_customer`
- Grain definition, business process, and measures
- Design decisions and justification
- Sample data flow from source system to warehouse

---

### 2. Schema Implementation
The warehouse schema is implemented in MySQL using the provided DDL.

**File:** `warehouse_schema.sql`

Includes:
- Dimension tables with surrogate keys
- Fact table with foreign key relationships
- Referential integrity enforcement

---

### 3. Warehouse Data Population
Realistic sample data is inserted to simulate business activity.

**File:** `warehouse_data.sql`

Data coverage:
- `dim_date`: 30 dates (January–February 2024)
- `dim_product`: 15 products across multiple categories
- `dim_customer`: 12 customers across different cities and segments
- `fact_sales`: 40 sales transactions with realistic quantities and pricing patterns

---

### 4. OLAP Analytics Queries
Business-focused analytical queries are written to demonstrate reporting and analysis capabilities.

**File:** `analytics_queries.sql`

Queries included:
1. Monthly sales drill-down analysis (Year → Quarter → Month)
2. Top 10 products by revenue with contribution percentage
3. Customer value segmentation (High / Medium / Low)

---

## How to Run (MySQL)

```bash
# Create the data warehouse database
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Create schema
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql

# Load warehouse data
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql

# Run analytics queries
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql

Key Learnings
•	Practical implementation of star schema modeling
•	Use of surrogate keys and dimensional design principles
•	Writing OLAP queries for drill-down, aggregation, and segmentation
•	Designing warehouse data for analytical performance

Notes
•	All SQL scripts run without foreign key violations
•	Data values are intentionally varied to reflect real-world sales behavior
•	This warehouse supports extensibility for additional dimensions and facts


