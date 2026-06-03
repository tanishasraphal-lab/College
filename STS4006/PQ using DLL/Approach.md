# Priority Queue Using Doubly Linked List in Java

## Aim
To implement a Priority Queue using a Doubly Linked List in Java.

## Description
A Priority Queue is a special type of queue where each element is associated with a priority. Elements are stored in sorted order based on their priority.

In this implementation:
- Each node stores data and priority.
- Lower priority value indicates higher priority.
- A Doubly Linked List is used to maintain the queue.
- Elements are inserted at their appropriate position according to priority.

## Algorithm

### Insertion
1. Create a new node with data and priority.
2. If the queue is empty, make the new node the front and rear.
3. If the new node has higher priority than the front node, insert it at the beginning.
4. Otherwise, traverse the list to find the correct position.
5. Insert the node while maintaining the sorted order of priorities.
6. Update the previous and next pointers accordingly.

### Traversal
1. Start from the front node.
2. Visit each node one by one.
3. Display its data and priority.
4. Continue until the end of the list.

## Time Complexity

| Operation | Complexity |
|------------|------------|
| Insertion | O(n) |
| Traversal | O(n) |


## Sample Input

```
Enter number of elements: 5
Enter data and priority:
10 3
Enter data and priority:
20 1
Enter data and priority:
30 2
Enter data and priority:
40 5
Enter data and priority:
50 4
```

## Sample Output

```
Elements in the Priority Queue:
(20, 1) (30, 2) (10, 3) (50, 4) (40, 5)
```

## Conclusion
The Priority Queue was successfully implemented using a Doubly Linked List. The elements are automatically arranged according to their priority, ensuring that higher-priority elements are processed before lower-priority elements.