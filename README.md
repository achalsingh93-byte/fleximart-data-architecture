# FlexiMart Data Architecture Project

**Student Name:** Achal Singh  
**Student ID:** BITSOM_BA_25071618  
**Email:** achalsingh93@gmail.com  
**Date:** 31-12-2025

---

## Project Overview

This project implements an end-to-end data architecture solution for FlexiMart, covering relational database ETL, NoSQL document modeling, and data warehouse analytics. The solution enables structured data ingestion, flexible product catalog management, and historical sales analysis using dimensional modeling and OLAP queries.

---

## Repository Structure

fleximart-data-architecture/
│
├── data/
│ ├── customers_raw.csv
│ ├── products_raw.csv
│ └── sales_raw.csv
│
├── part1-database-etl/
│ ├── README.md
│ ├── etl_pipeline.py
│ ├── schema_documentation.md
│ ├── business_queries.sql
│ └── data_quality_report.txt
│
├── part2-nosql/
│ ├── README.md
│ ├── nosql_analysis.md
│ ├── mongodb_operations.js
│ └── products_catalog.json
│
├── part3-datawarehouse/
│ ├── README.md
│ ├── star_schema_design.md
│ ├── warehouse_schema.sql
│ ├── warehouse_data.sql
│ └── analytics_queries.sql
│
├── .gitignore
└── README.md


---


---

## Technologies Used

- Python 3.x, pandas, pymysql  
- MySQL 8.0  
- MongoDB 6.0  
- Git & GitHub  

---

## Setup Instructions

### Database Setup

```bash
# Create databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

# Run Part 1 - ETL Pipeline
python part1-database-etl/etl_pipeline.py

# Run Part 1 - Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

# Run Part 3 - Data Warehouse Schema and Data
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql

MongoDB Setup

mongosh < part2-nosql/mongodb_operations.js

```
Key Learnings
•	Designed and implemented an end-to-end ETL pipeline using Python and MySQL
•	Applied document-oriented modeling concepts using MongoDB
•	Built a star schema data warehouse and performed OLAP analytics
•	Understood trade-offs between relational, NoSQL, and analytical data models

Challenges Faced

=>Handling inconsistent raw data formats during ETL, resolved through validation and data quality checks

=>Designing an optimal star schema to support drill-down and roll-up analytics while avoiding redundancy