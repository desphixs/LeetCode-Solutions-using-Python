To solve this problem step by step, here's a clear breakdown of the procedure you should follow:

### 1. **Understand the Goal**

-   You need to **remove duplicates** from a sorted array, keeping the unique elements **in-place**.
-   The array is sorted in non-decreasing order.
-   You need to return `k`, which is the count of unique elements, and the first `k` elements of the array should contain these unique elements in the original order.

### 2. **Think of a Two-Pointer Approach**

Since the array is sorted, you can leverage this fact by using two pointers:

-   One pointer (`i`) will iterate over the array.
-   Another pointer (`j`) will keep track of the **position where the next unique element should be placed**.

### 3. **Initialize the Pointers**

-   Set the first pointer (`j`) to `0`, since the first element is always unique.
-   Start the second pointer (`i`) from `1` to traverse the array from the second element onward.

### 4. **Traverse the Array and Compare Elements**

-   For each element at position `i`, compare it with the element at position `j`.
-   If the element at `i` is **different** from the element at `j` (i.e., a new unique element):
    -   Increment the `j` pointer (move it forward to make space for the new unique element).
    -   Assign the element at `i` to the `j` position (overwrite the old element at `j` with the new unique one).

### 5. **Continue This Process**

-   Repeat the above step until you've gone through all the elements in the array.
-   At the end, the `j` pointer will indicate the index of the last unique element. So, the count of unique elements (`k`) will be `j + 1` (because array indices start at `0`).

### 6. **Return the Count of Unique Elements (`k`)**

-   After completing the traversal, return `k`, which is the number of unique elements, and the first `k` elements of the array will be your answer.

### Example Walkthrough:

Let's take an example to illustrate the process:

#### Input:

`nums = [0, 0, 1, 1, 2, 2, 3, 3, 4]`

#### Step-by-Step Execution:

1. Start with pointers: `j = 0`, `i = 1`.

    - `nums[j] = 0`, `nums[i] = 0` → They are the same, so skip.

2. Move `i` to the next position: `i = 2`.

    - `nums[j] = 0`, `nums[i] = 1` → They are different, so:
        - Increment `j`: `j = 1`.
        - Update `nums[j]` to `nums[i]` → `nums = [0, 1, 1, 1, 2, 2, 3, 3, 4]`.

3. Move `i` to the next position: `i = 3`.

    - `nums[j] = 1`, `nums[i] = 1` → They are the same, so skip.

4. Move `i` to the next position: `i = 4`.
    - `nums[j] = 1`, `nums[i] = 2` → They are different, so:
        - Increment `j`: `j = 2`.
        - Update `nums[j]` to `nums[i]` → `nums = [0, 1, 2, 1, 2, 2, 3, 3, 4]`.

... And continue this process until you've gone through the entire array.

#### Final Result:

After the loop, you'll have `nums = [0, 1, 2, 3, 4, _, _, _, _]` and `k = 5`, where the first 5 elements are the unique ones.

---

### Summary of Steps:

1. Initialize two pointers: `j = 0`, and `i = 1`.
2. Traverse the array with `i` from 1 to the end.
3. If `nums[i] != nums[j]`, increment `j` and copy `nums[i]` to `nums[j]`.
4. Continue until all elements are processed.
5. Return `j + 1` as the number of unique elements (`k`).

This step-by-step approach will help you tackle this problem.
