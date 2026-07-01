// ==============================
// MongoDB CRUD Operations
// Database: courseDB
// Collection: students
// ==============================

// Create / Switch Database
db = db.getSiblingDB("courseDB");

// Create Collection
db.createCollection("students");

// Insert One Record
db.students.insertOne({
    student_id: 1,
    name: "Ravi",
    course: "Java",
    fee: 8000
});

// Insert Four Records
db.students.insertMany([
    {
        student_id: 2,
        name: "Anil",
        course: "Python",
        fee: 6500
    },
    {
        student_id: 3,
        name: "Priya",
        course: "C++",
        fee: 9000
    },
    {
        student_id: 4,
        name: "Rahul",
        course: "Web",
        fee: 3500
    },
    {
        student_id: 5,
        name: "Neha",
        course: "AI",
        fee: 7500
    }
]);

// Display All Records
print("\n----- All Students -----");
db.students.find();

// Find students with fee > 7000
print("\n----- Fee Greater Than 7000 -----");
db.students.find({ fee: { $gt: 7000 } });

// Update Ravi's fee to 9000
print("\n----- Update Ravi's Fee -----");
db.students.updateOne(
    { name: "Ravi" },
    { $set: { fee: 9000 } }
);

// Display after Update
db.students.find();

// Increase fee of all students by 500
print("\n----- Increase Fee by 500 -----");
db.students.updateMany(
    {},
    { $inc: { fee: 500 } }
);

// Display after Increase
db.students.find();

// Delete students with fee less than 4000
print("\n----- Delete Fee < 4000 -----");
db.students.deleteMany(
    { fee: { $lt: 4000 } }
);

// Final Records
print("\n----- Final Student Records -----");
db.students.find();