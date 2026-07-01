use('companyDB')

db.createCollection("employees")

db.employees.insertOne({
emp_id:1,
name:"Alice",
department:"HR",
salary:30000
})

db.employees.insertMany([
{
emp_id:2,
name:"Bob",
department:"Sales",
salary:20000
},
{
emp_id:3,
name:"David",
department:"IT",
salary:40000
},
{
emp_id:4,
name:"John",
department:"Finance",
salary:12000
},
{
emp_id:5,
name:"Mary",
department:"HR",
salary:28000
}
])

db.employees.find({salary:{$gt:25000}})

db.employees.updateOne(
{name:"Alice"},
{$set:{salary:35000}}
)

db.employees.updateMany(
{},
{$inc:{salary:2000}}
)

db.employees.deleteMany(
{salary:{$lt:15000}}
)

db.employees.find()