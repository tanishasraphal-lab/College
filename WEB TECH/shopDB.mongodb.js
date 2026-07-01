// Create Database
use('shopDB')

// Create Collection
db.createCollection("products")

// Insert One Record
db.products.insertOne({
product_id:1,
name:"Laptop",
category:"Electronics",
price:60000
})

// Insert Four Records
db.products.insertMany([
{
product_id:2,
name:"Mobile",
category:"Electronics",
price:30000
},
{
product_id:3,
name:"Chair",
category:"Furniture",
price:8000
},
{
product_id:4,
name:"TV",
category:"Electronics",
price:55000
},
{
product_id:5,
name:"Table",
category:"Furniture",
price:12000
}
])

// ii. Find products price >50000
db.products.find({price:{$gt:50000}})

// iii. Update Laptop price to 65000
db.products.updateOne(
{name:"Laptop"},
{$set:{price:65000}}
)

// iv. Increase all prices by 1000
db.products.updateMany(
{},
{$inc:{price:1000}}
)

// v. Delete products price <10000
db.products.deleteMany(
{price:{$lt:10000}}
)

// Display Records
db.products.find()