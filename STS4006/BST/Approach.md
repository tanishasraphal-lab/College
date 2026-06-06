# Approach: Binary Tree Creation and Inorder Traversal

## Objective
Construct a binary tree from a level-order input representation and perform an inorder traversal to display the nodes.

## Steps

### 1. Input Collection
- Read the tree elements as a single line of input.
- The input represents the binary tree in level-order format.
- Use `"N"` to indicate a null (missing) node.

### 2. Tree Construction
- If the first element is `"N"`, the tree is empty.
- Create the root node using the first element.
- Use a queue to build the tree level by level.
- Insert the root node into the queue.

### 3. Level-Order Processing
- While the queue is not empty:
  - Remove the front node from the queue.
  - Read the next element for the left child.
    - If it is not `"N"`, create a new node and attach it as the left child.
    - Add the new node to the queue.
  - Read the next element for the right child.
    - If it is not `"N"`, create a new node and attach it as the right child.
    - Add the new node to the queue.
- Continue until all input elements are processed.

### 4. Inorder Traversal
- Visit the left subtree recursively.
- Process the current node.
- Visit the right subtree recursively.

### 5. Output
- Print the nodes in inorder sequence.

## Data Structures Used
- **Binary Tree Node**
  - Stores node data.
  - Contains references to left and right children.

- **Queue**
  - Used during tree construction to process nodes level by level.

## Time Complexity
- Tree Construction: **O(n)**
- Inorder Traversal: **O(n)**

## Space Complexity
- Queue Storage: **O(n)**
- Recursive Call Stack (Traversal): **O(h)**, where `h` is the height of the tree.