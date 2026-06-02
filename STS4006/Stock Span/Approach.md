# Stock Span Problem

## Approach

The Stock Span Problem is solved efficiently using a **Stack**.

### Idea
For each day's stock price, find the number of consecutive previous days (including the current day) for which the stock price was less than or equal to the current day's price.

### Algorithm
1. Create an empty stack to store indices of stock prices.
2. For each day `i`:
   - Pop elements from the stack while the price at the top index is less than or equal to the current price.
   - If the stack becomes empty, the span is `i + 1`.
   - Otherwise, the span is `i - stack.peek()`.
   - Push the current index onto the stack.
3. Print the span array.

### Pseudocode

```text
Initialize an empty stack

for i = 0 to n-1
    while stack is not empty and
          price[stack.top()] <= price[i]
        stack.pop()

    if stack is empty
        span[i] = i + 1
    else
        span[i] = i - stack.top()

    stack.push(i)
```

### Complexity Analysis

- Time Complexity: O(n)
- Space Complexity: O(n)

### Example

Input:

```text
Prices = [100, 80, 60, 70, 60, 75, 85]
```

Output:

```text
Span = [1, 1, 1, 2, 1, 4, 6]
```