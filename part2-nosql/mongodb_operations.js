/* 
MongoDB Operations for FlexiMart Product Catalog
Database: fleximart
Collection: products
*/

/* 1. Switch to database */
use fleximart;

/* 2. Insert products from JSON file */
db.products.insertMany([
  /* products_catalog.json content imported here */
]);

/* 3. Find all products in Electronics category */
db.products.find(
  { category: "Electronics" },
  { name: 1, price: 1, stock: 1, _id: 0 }
);

/* 4. Find products with price greater than 50,000 */
db.products.find(
  { price: { $gt: 50000 } },
  { name: 1, category: 1, price: 1, _id: 0 }
);

/* 5. Find products with average rating >= 4 */
db.products.aggregate([
  {
    $addFields: {
      avgRating: { $avg: "$reviews.rating" }
    }
  },
  {
    $match: {
      avgRating: { $gte: 4 }
    }
  },
  {
    $project: {
      name: 1,
      category: 1,
      avgRating: 1,
      _id: 0
    }
  }
]);

/* 6. Count products by category */
db.products.aggregate([
  {
    $group: {
      _id: "$category",
      totalProducts: { $sum: 1 }
    }
  }
]);

/* 7. Find products that are low in stock (less than 50) */
db.products.find(
  { stock: { $lt: 50 } },
  { name: 1, stock: 1, _id: 0 }
);

/* 8. Find products having tag '5G' */
db.products.find(
  { tags: "5G" },
  { name: 1, tags: 1, _id: 0 }
);

/* 9. Update stock after a sale */
db.products.updateOne(
  { product_id: "ELEC001" },
  { $inc: { stock: -1 } }
);

/* 10. Add a new review to a product */
db.products.updateOne(
  { product_id: "FASH001" },
  {
    $push: {
      reviews: {
        user_id: "U031",
        username: "NewBuyer",
        rating: 5,
        comment: "Excellent quality and fit!",
        date: "2024-03-30"
      }
    }
  }
);
