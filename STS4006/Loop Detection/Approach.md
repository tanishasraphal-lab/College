# Loop Detection in Linked List using Floyd's Cycle Detection Algorithm

## Approach

This program detects whether a loop (cycle) exists in a singly linked list using **Floyd's Cycle Detection Algorithm**, also known as the **Tortoise and Hare Algorithm**.

### Step 1: Create the Linked List

* Define a `Node` class containing:

  * `data` to store the node value.
  * `next` to store the reference to the next node.
* Use the `push()` method to insert nodes at the beginning of the linked list.

### Step 2: Create a Loop (Optional)

* Ask the user whether a loop should be created.
* If the user selects **'y'**:

  * Traverse to the last node of the linked list.
  * Find the node at the specified position.
  * Connect the last node to that node, creating a loop.

### Step 3: Detect the Loop

* Initialize two pointers:

  * `slow` pointer moves one node at a time.
  * `fast` pointer moves two nodes at a time.
* Traverse the linked list while `fast` and `fast.next` are not `null`.
* If at any point `slow` and `fast` point to the same node, a loop is present.
* If `fast` reaches `null`, the linked list does not contain a loop.

### Step 4: Display the Result

* Print **"Loop found"** if a cycle is detected.
* Otherwise, print **"Loop not found"**.

## Algorithm

1. Create an empty linked list.
2. Insert nodes using the `push()` method.
3. Optionally create a loop based on user input.
4. Initialize `slow` and `fast` pointers to the head node.
5. Move `slow` by one step and `fast` by two steps.
6. If `slow == fast`, return **Loop Found**.
7. If `fast` or `fast.next` becomes `null`, return **Loop Not Found**.
8. Print the result.

## Time Complexity

* **O(n)**

## Space Complexity

* **O(1)**

The algorithm efficiently detects loops using only two pointers and does not require any extra memory.
