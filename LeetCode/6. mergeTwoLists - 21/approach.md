### **Approach:**

The approach used to solve this problem is the **Two-Pointer Merge Technique**, commonly used in merge operations for sorted lists or arrays (similar to the merge step of merge sort).

1. **Two-Pointer Merge**:

    - Two pointers, `list1` and `list2`, are used to traverse both linked lists.
    - At each step, the smaller value between the two lists is selected, and that node is linked to the result list.
    - The pointers (`list1` and `list2`) are advanced after each comparison, continuing until one of the lists is fully traversed.

2. **Handling Remainders**:
    - Once one list is exhausted, the remainder of the other list (which is already sorted) is appended directly to the result list.
