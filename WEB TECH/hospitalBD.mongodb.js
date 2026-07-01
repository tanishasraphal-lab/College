// Create Database
use('hospitalDB')

// Create Collection
db.createCollection("patients")

// Insert One Record
db.patients.insertOne({
patient_id:1,
name:"Bob",
age:30,
bill:2000
})

// Insert Four Records
db.patients.insertMany([
{
patient_id:2,
name:"Alice",
age:25,
bill:1500
},
{
patient_id:3,
name:"David",
age:40,
bill:800
},
{
patient_id:4,
name:"John",
age:35,
bill:3000
},
{
patient_id:5,
name:"Mary",
age:29,
bill:1800
}
])

// ii. Find patients bill >1500
db.patients.find({bill:{$gt:1500}})

// iii. Update Bob bill to 2500
db.patients.updateOne(
{name:"Bob"},
{$set:{bill:2500}}
)

// iv. Increase bill by 500
db.patients.updateMany(
{},
{$inc:{bill:500}}
)

// v. Delete patients bill <1000
db.patients.deleteMany(
{bill:{$lt:1000}}
)

// Display Records
db.patients.find()