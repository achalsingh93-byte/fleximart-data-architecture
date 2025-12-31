# Part 2: NoSQL Data Modeling and Analysis (MongoDB)

## Overview
This part demonstrates the use of a NoSQL database (MongoDB) to manage the FlexiMart product catalog.  
The dataset contains semi-structured product data with nested specifications, embedded reviews, and flexible attributes.

MongoDB is chosen for its document-oriented model, which naturally supports this structure.

---

## Files Included

| File | Description |
|-----|------------|
| products_catalog.json | Product catalog dataset in JSON format |
| nosql_analysis.md | NoSQL data modeling and design justification |
| mongodb_operations.js | MongoDB queries and operations |

---

## Database Design

- Database Name: `fleximart`
- Collection Name: `products`
- One document per product
- Embedded documents for specifications and reviews
- Arrays for tags and sizes

---

## Key Operations Demonstrated

- Insert product documents
- Category-based filtering
- Price-based queries
- Aggregation for average ratings
- Inventory monitoring
- Embedded document updates

---

## How to Run

1. Start MongoDB server
2. Open MongoDB shell
3. Switch to project directory
4. Execute:
   ```bash
   mongosh < mongodb_operations.js
