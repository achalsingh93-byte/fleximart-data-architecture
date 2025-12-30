# FlexiMart Data Architecture Assignment

## Part 1: Relational Database ETL (MySQL)

This project implements an end-to-end ETL pipeline using Python and MySQL.

### Features
- Raw data ingestion from CSV files using pandas
- Data cleaning and transformation
- Relational schema design in MySQL
- Table creation and data loading
- Business analytics queries using SQL

### Folder Structure
- data/ : Raw CSV datasets
- part1-database-etl/etl_pipeline.py : Python ETL script
- part1-database-etl/business_queries.sql : Business SQL queries

### How to Run
1. Create MySQL database `fleximart`
2. Update database credentials in `etl_pipeline.py`
3. Run:
   ```bash
   python part1-database-etl/etl_pipeline.py
Data verification is performed using MySQL Workbench.