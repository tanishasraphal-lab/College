# Approach: Right View of Binary Tree from Level Order Input

## Objective

Construct a binary tree from a level-order traversal input and print its right view.

## Algorithm Overview

The solution consists of two major parts:

1. Building the Binary Tree
2. Finding the Right View of the Tree

---

## Part 1: Building the Binary Tree

### Idea

The tree is provided as a sequence of node values in level order. The keyword `"null"` represents a missing node.

### Steps

1. If the input is empty or the first value is `"null"`, return an empty tree.
2. Create the root node using the first value.
3. Use a queue to keep track of nodes whose children are yet to be assigned.
4. Insert the root into the queue.
5. Process the remaining values one by one:

   * Remove a node from the queue.
   * Assign the next value as its left child if it is not `"null"`.
   * Assign the following value as its right child if it is not `"null"`.
   * Add newly created child nodes to the queue.
6. Continue until all input values are processed.

### Example Input

1 2 3 null 5 null 4

Constructed Tree:

```
    1
   / \
  2   3
   \   \
    5   4
```

---

## Part 2: Finding the Right View

### Idea

Perform a Level Order Traversal (Breadth-First Search). At every level, the last node encountered is visible from the right side.

### Steps

1. If the tree is empty, return an empty list.
2. Create a queue and insert the root node.
3. While the queue is not empty:

   * Determine the number of nodes present at the current level.
   * Process all nodes of that level.
   * Store the value of the last node processed at that level.
   * Insert the left and right children of each node into the queue.
4. Repeat until all levels are processed.
5. Return the collected nodes as the right view.

### Example

Tree:

```
    1
   / \
  2   3
   \   \
    5   4
```

Level-wise Processing:

* Level 1 → 1 → Right View Node = 1
* Level 2 → 2, 3 → Right View Node = 3
* Level 3 → 5, 4 → Right View Node = 4

Output:

Right View: 1 3 4

---

## Time Complexity

### Tree Construction

* O(n)

### Right View Traversal

* O(n)

### Total

* O(n)

where `n` is the number of nodes in the tree.

---

## Space Complexity

### Queue during Construction

* O(n)

### Queue during BFS Traversal

* O(n)

### Result List

* O(h) to O(n), where `h` is the height of the tree.

Overall Space Complexity:

* O(n)

---

## Data Structures Used

* Binary Tree
* Queue (LinkedList)
* ArrayList

---

## Key Concept

During level-order traversal, the last node visited at every level represents the node visible from the right side. Collecting these nodes level by level produces the Right View of the Binary Tree.
