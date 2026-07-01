// Create Database
use('university')

// Create Collection
db.createCollection("students")

// Insert One Document
db.students.insertOne({
ID:1,
name:"Alice",
age:20,
department:"CSE",
marks:85
})

// Insert Multiple Records
db.students.insertMany([
{
ID:2,
name:"Bob",
age:21,
department:"ECE",
marks:78
},
{
ID:3,
name:"Charlie",
age:22,
department:"CSE",
marks:92
},
{
ID:4,
name:"David",
age:20,
department:"IT",
marks:48
},
{
ID:5,
name:"Eva",
age:19,
department:"AI",
marks:88
}
])

// ii. Find students marks > 80
db.students.find(
{marks:{$gt:80}}
)

// iii. Update Alice marks to 90
db.students.updateOne(
{name:"Alice"},
{$set:{marks:90}}
)

// iv. Increase marks by 5
db.students.updateMany(
{},
{$inc:{marks:5}}
)

// v. Delete students marks < 50
db.students.deleteMany(
{marks:{$lt:50}}
)

// Display records
db.students.find()