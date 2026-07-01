use("University_DB");

// Create Collection
 db.createCollection("Students");

// Insert Initial Documents
db.Students.insertMany([
  { rollNumber: 1, name: "Alice", age: 20, cgpa: 8.5 },
  { rollNumber: 2, name: "Bob", age: 21, cgpa: 7.8 },
  { rollNumber: 3, name: "Charlie", age: 19, cgpa: 9.0 }
]);

// Insert David
db.Students.insertOne({
  rollNumber: 4,
  name: "David",
  age: 22,
  cgpa: 8.2
});

// Insert Multiple Students
db.Students.insertMany([
  { rollNumber: 5, name: "Eve", age: 20, cgpa: 7.9 },
  { rollNumber: 6, name: "Frank", age: 23, cgpa: 8.0 }
]);

// Find All Students 1st
db.Students.find();    

// Find Alice 2nd
db.Students.find({ name: "Alice" }); 

// Find Students Older than 20 3rd
db.Students.find({ age: { $gt: 20 } }); 

// Find Students with CGPA > 8.0 4th
db.Students.find({ cgpa: { $gt: 8.0 } }); 

// Find Students with CGPA between 7.5 and 9.0 5th
db.Students.find({   
  cgpa: {
    $gte: 7.5,
    $lte: 9.0
  }
});

// Update Alice's CGPA
db.Students.updateOne(
  { name: "Alice" },
  { $set: { cgpa: 8.7 } }
);

// Increase CGPA by 0.2 where CGPA < 8.0
db.Students.updateMany(
  { cgpa: { $lt: 8.0 } },
  { $inc: { cgpa: 0.2 } }
);

// Delete Bob
db.Students.deleteOne({ name: "Bob" });

// Delete Students with CGPA < 7.5
db.Students.deleteMany({
  cgpa: { $lt: 7.5 }
});

// Display Final Collection
db.Students.find();
