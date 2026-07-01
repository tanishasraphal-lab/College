db = db.getSiblingDB("courseDB");

db.createCollection("students");

db.students.insertOne({
    student_id: 1,
    name: "Bob",
    course: "Java",
    fee: 5000
});

db.students.insertMany([
    {
        student_id: 2,
        name: "Alice",
        course: "Python",
        fee: 7000
    },
    {
        student_id: 3,
        name: "David",
        course: "C",
        fee: 9000
    },
    {
        student_id: 4,
        name: "John",
        course: "Web",
        fee: 4500
    },
    {
        student_id: 5,
        name: "Mary",
        course: "AI",
        fee: 8500
    }
]);

// Find students whose fee is greater than 8000
db.students.find({ fee: { $gt: 8000 } });

// Update Bob's fee to 9000
db.students.updateOne(
    { name: "Bob" },
    { $set: { fee: 9000 } }
);

// Increase fee of all students by 1000
db.students.updateMany(
    {},
    { $inc: { fee: 1000 } }
);

// Delete students whose fee is less than 5000
db.students.deleteMany(
    { fee: { $lt: 5000 } }
);

// Display all students
db.students.find();