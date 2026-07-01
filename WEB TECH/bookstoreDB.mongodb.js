// Create Database
use('bookstore')

// Create Collection
db.createCollection("books")

// Insert One Document
db.books.insertOne({
    book_id:1,
    title:"Python",
    author:"John Smith",
    price:450
})

// Insert Four Records
db.books.insertMany([
{
book_id:2,
title:"Java",
author:"James",
price:350
},
{
book_id:3,
title:"C Programming",
author:"Dennis",
price:500
},
{
book_id:4,
title:"Data Structures",
author:"Mark",
price:600
},
{
book_id:5,
title:"Web Technology",
author:"David",
price:180
}
])

// ii. Find books price > 400
db.books.find({price:{$gt:400}})

// iii. Update Python price to 500
db.books.updateOne(
{title:"Python"},
{$set:{price:500}}
)

// iv. Increase all prices by 50
db.books.updateMany(
{},
{$inc:{price:50}}
)

// v. Delete books price < 200
db.books.deleteMany(
{price:{$lt:200}}
)

// Display records
db.books.find()