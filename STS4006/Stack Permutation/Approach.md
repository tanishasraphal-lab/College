# Stack Permutation Check in Java

## Problem Statement
Given two arrays `a` and `b` of size `n`, determine whether array `b` can be obtained from array `a` using stack operations (push and pop).

A stack permutation is possible if elements of `a` can be pushed into a stack and popped in such a way that the output sequence matches `b`.

---

## Approach

1. Read the size `n`.
2. Input the elements of arrays `a` and `b`.
3. Create an empty stack.
4. Traverse array `a`:
   - Push each element into the stack.
   - After every push, check whether the top of the stack matches the current element in `b`.
   - If it matches, pop the element and move to the next element in `b`.
5. After processing all elements:
   - If the stack is empty, the permutation is valid.
   - Otherwise, it is not possible.

---

## Algorithm

1. Push elements of array `a` one by one into the stack.
2. While the stack is not empty and the top element equals the current element in `b`:
   - Pop the element.
   - Increment pointer `j`.
3. After all elements are processed:
   - Return `true` if the stack is empty.
   - Otherwise return `false`.

---

## Time Complexity

- **O(n)**

Each element is pushed and popped at most once.

## Space Complexity

- **O(n)**

Extra space is required for the stack.

---


## Sample Input

```
Enter number of elements:
5

Enter elements of a:
1 2 3 4 5

Enter elements of b:
4 5 3 2 1
```

## Sample Output

```
Result: true
```

---

## Example Explanation

Array `a` = `[1, 2, 3, 4, 5]`

Desired output `b` = `[4, 5, 3, 2, 1]`

Stack Operations:

```
Push 1
Push 2
Push 3
Push 4
Pop 4

Push 5
Pop 5
Pop 3
Pop 2
Pop 1
```

Output sequence becomes:

```
4 5 3 2 1
```

Since it matches array `b`, the result is `true`.