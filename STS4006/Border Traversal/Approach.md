# Boundary Traversal of Binary Tree

## Intuition

Boundary Traversal of a Binary Tree involves visiting all the boundary nodes of the tree in an anti-clockwise direction. The traversal is divided into three main parts:

1. **Left Boundary (excluding leaf nodes)** – Nodes encountered while moving from the root towards the leftmost node.
2. **Leaf Nodes (from left to right)** – All leaf nodes present in the tree.
3. **Right Boundary (excluding leaf nodes, in reverse order)** – Nodes encountered while moving from the rightmost node back towards the root.

The main idea is to traverse only the boundary nodes efficiently while ensuring that no node is printed more than once.

## Approach

### Step 1: Print the Root Node

* Start the traversal from the root.
* If the tree is empty, return immediately.

### Step 2: Traverse the Left Boundary

* Begin from the left child of the root.
* Print all non-leaf nodes encountered.
* Prefer moving to the left child.
* If a left child does not exist, move to the right child.
* Do not print leaf nodes to avoid duplication.

### Step 3: Traverse all Leaf Nodes

* Recursively traverse the entire tree.
* Print every node that has no left and right children.
* Visit leaves from left to right order.

### Step 4: Traverse the Right Boundary

* Begin from the right child of the root.
* Prefer moving to the right child.
* If a right child does not exist, move to the left child.
* Exclude leaf nodes.
* Store the nodes using recursion and print them while returning so that they appear in reverse order.

### Step 5: Avoid Duplicate Nodes

* Ensure that leaf nodes are printed only during leaf traversal.
* Exclude leaf nodes from both left and right boundary traversals.

## Key Points

* Left Boundary: Root → Leftmost node (excluding leaves).
* Leaf Nodes: All leaves from left to right.
* Right Boundary: Rightmost node → Root (excluding leaves and printed in reverse).
* Every boundary node is visited exactly once.
* Leaf nodes are not duplicated.

## Algorithm

1. Print the root node.
2. Traverse and print the left boundary excluding leaf nodes.
3. Traverse and print all leaf nodes.
4. Traverse the right boundary excluding leaf nodes and print them in reverse order.
5. Combine all parts to obtain the complete boundary traversal.

## Example

Input Tree:
1
/ 
2   3
/ \ / 
4  5 6  7

Boundary Traversal:
1 2 4 5 6 7 3

## Time Complexity

* Left Boundary Traversal: O(H)
* Leaf Traversal: O(N)
* Right Boundary Traversal: O(H)

Overall Time Complexity: **O(N)**

where N is the number of nodes in the tree.

## Space Complexity

Overall Space Complexity: **O(H)**

where H is the height of the tree due to the recursion stack.

## Other Possible Approaches

### Recursive Approach

* Use separate recursive functions for left boundary, leaf nodes, and right boundary traversal.
* Simple and easy to implement.
* May lead to higher recursion depth in skewed trees.

### Level Order Approach

* Use Breadth-First Search (BFS) to process nodes level by level.
* Requires visiting many unnecessary nodes.
* Less efficient than dedicated boundary traversal methods.

## Applications

### Visualization and Graphical Representations

* Used in tree rendering and diagram generation.

### Geographical Mapping

* Helps identify boundary elements in terrain and map structures.

### Network Routing

* Useful for visualizing outer communication paths in tree-based network topologies.

### Artificial Intelligence and Decision Trees

* Helps identify key decision points and boundary nodes in hierarchical decision models.
