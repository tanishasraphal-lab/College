# Approach: Right View of Binary Tree

## Objective

Print the nodes visible when the binary tree is viewed from the right side.

## Algorithm Used

**Level Order Traversal (Breadth-First Search - BFS)** using a Queue.

## Steps

1. Check if the tree is empty.

   * If the root is `null`, return immediately.

2. Create a queue and insert the root node into it.

3. Traverse the tree level by level:

   * Find the number of nodes present at the current level (`size`).
   * Process all nodes of that level one by one.

4. For each node in the current level:

   * Remove the node from the queue.
   * If it is the last node of that level, print its value because it represents the rightmost node visible from the right side.
   * Insert its left child into the queue if it exists.
   * Insert its right child into the queue if it exists.

5. Repeat the process until the queue becomes empty.

## Example

Binary Tree:

```
    1
   / \
  2   3
   \   \
    5   4
```

Level-wise traversal:

* Level 1 → 1 → Right View Node = 1
* Level 2 → 2, 3 → Right View Node = 3
* Level 3 → 5, 4 → Right View Node = 4

Output:

Right View: 1 3 4

## Time Complexity

* **O(n)**, where `n` is the number of nodes in the tree.

## Space Complexity

* **O(n)** in the worst case for the queue used during level-order traversal.

## Data Structures Used

* Binary Tree
* Queue (LinkedList implementation)

## Key Idea

During level-order traversal, the last node processed at every level is the node visible from the right side. Printing these last nodes gives the Right View of the Binary Tree.
