### Time Complexity:

-   The solution loops through the entire array exactly once.
-   The comparison and update operations (i.e., `if nums[i] == nums[j]`, and `nums[j] = nums[i]`) are performed in constant time (`O(1)`).

Since the loop runs from index `1` to the end of the array, the overall time complexity is:

-   **O(n)**, where `n` is the length of the input array `nums`.

### Space Complexity:

-   The solution uses **in-place** modification of the `nums` array.
-   You're only using two pointers (`i` and `j`) and a few temporary variables for comparison.

Thus, the space complexity is:

-   **O(1)**, because the algorithm does not use any additional space that grows with the size of the input.

### Final Complexity:

-   **Time complexity**: `O(n)`
-   **Space complexity**: `O(1)`
