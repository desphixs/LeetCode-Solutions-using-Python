### **Time Complexity:**

-   **O(n + m)** where `n` is the number of nodes in `list1` and `m` is the number of nodes in `list2`.
    -   We iterate through both linked lists once, comparing and merging their nodes. Since each node in both lists is processed exactly once, the time complexity is linear with respect to the total number of nodes in both lists.

### **Space Complexity:**

-   **O(1)** (constant space, aside from the input/output)

    -   The merging is done in-place, meaning we only modify the `next` pointers of the nodes from `list1` and `list2` without creating any additional data structures (like arrays).
    -   The only extra space used is for the `dummy` node, and a few pointers (`current`, `list1`, and `list2`), which is considered constant space.

-   **Note**: The input/output representation of linked lists (i.e., Python lists) used for testing is not part of the algorithm's space complexity, which refers specifically to the space used during the merging process itself.

### **Summary:**

-   **Time Complexity**: O(n + m)
-   **Space Complexity**: O(1)
-   **Approach**: Two-Pointer Merge Technique
