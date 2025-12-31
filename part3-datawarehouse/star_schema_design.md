# Star Schema Design – FlexiMart Data Warehouse

## Section 1: Schema Overview

### FACT TABLE: fact_sales

**Grain:**  
One row per product per order line item.

**Business Process:**  
Sales transactions capturing each product sold per order.

**Measures (Numeric Facts):**
- quantity_sold: Number of units sold
- unit_price: Price per unit at time of sale
- discount_amount: Discount applied
- total_amount: Final amount  
  (quantity_sold × unit_price − discount_amount)

**Foreign Keys:**
- date_key → dim_date
- product_key → dim_product
- customer_key → dim_customer

---

### DIMENSION TABLE: dim_date

**Purpose:**  
Date dimension for time-based analysis.

**Type:**  
Conformed dimension.

**Attributes:**
- date_key (PK): Surrogate key (YYYYMMDD)
- full_date: Actual date
- day_of_week: Monday, Tuesday, etc.
- day_of_month: Numeric day
- month: 1–12
- month_name: January, February, etc.
- quarter: Q1, Q2, Q3, Q4
- year: Calendar year
- is_weekend: Boolean indicator

---

### DIMENSION TABLE: dim_product

**Purpose:**  
Provides descriptive product attributes for sales analysis.

**Attributes:**
- product_key (PK): Surrogate key
- product_id: Business product identifier
- product_name: Product name
- category: Product category
- subcategory: Product subcategory
- unit_price: Standard product price

---

### DIMENSION TABLE: dim_customer

**Purpose:**  
Stores customer demographics and segmentation details.

**Attributes:**
- customer_key (PK): Surrogate key
- customer_id: Business customer identifier
- customer_name: Full customer name
- city: City of residence
- state: State of residence
- customer_segment: Customer classification

---

## Section 2: Design Decisions

The transaction line-item level granularity was selected to preserve maximum analytical flexibility. This enables detailed drill-down analysis by product, customer, and date while still supporting aggregation at higher levels such as monthly or yearly sales.

Surrogate keys are used instead of natural keys to ensure stability and performance. Business identifiers may change over time, but surrogate keys remain consistent and allow faster joins across fact and dimension tables.

This star schema supports both drill-down and roll-up operations efficiently. Analysts can drill down from year to quarter to month using the date dimension or roll up product-level sales to category-level summaries.

---

## Section 3: Sample Data Flow

### Source Transaction
Order #101  
Customer: John Doe  
Product: Laptop  
Quantity: 2  
Unit Price: ₹50,000  

---

### Data Warehouse Representation

#### fact_sales
```json
{
  "date_key": 20240115,
  "product_key": 5,
  "customer_key": 12,
  "quantity_sold": 2,
  "unit_price": 50000,
  "discount_amount": 0,
  "total_amount": 100000
}
{
  "date_key": 20240115,
  "full_date": "2024-01-15",
  "day_of_week": "Monday",
  "month": 1,
  "month_name": "January",
  "quarter": "Q1",
  "year": 2024,
  "is_weekend": false
}
{
  "product_key": 5,
  "product_name": "Laptop",
  "category": "Electronics",
  "subcategory": "Computers",
  "unit_price": 50000
}
{
  "customer_key": 12,
  "customer_name": "John Doe",
  "city": "Mumbai",
  "state": "Maharashtra",
  "customer_segment": "Retail"
}
