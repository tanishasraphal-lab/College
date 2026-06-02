## Approach

The Tower of Hanoi problem is solved using recursion.

### Algorithm
1. If there is only one disk (`n = 1`), move it directly from the source rod to the destination rod.
2. Move the top `n - 1` disks from the source rod to the auxiliary rod using the destination rod.
3. Move the largest disk from the source rod to the destination rod.
4. Move the `n - 1` disks from the auxiliary rod to the destination rod using the source rod.

### Pseudocode

```text
TowerOfHanoi(n, source, auxiliary, destination)

if n == 1
    Move disk 1 from source to destination
    return

TowerOfHanoi(n - 1, source, destination, auxiliary)

Move disk n from source to destination

TowerOfHanoi(n - 1, auxiliary, source, destination)
```

### Complexity Analysis

- Time Complexity: O(2^n)
- Space Complexity: O(n)
- Total Moves Required: 2^n - 1

### Working Example (n = 3)

```text
Move disk 1 from A to C
Move disk 2 from A to B
Move disk 1 from C to B
Move disk 3 from A to C
Move disk 1 from B to A
Move disk 2 from B to C
Move disk 1 from A to C
```