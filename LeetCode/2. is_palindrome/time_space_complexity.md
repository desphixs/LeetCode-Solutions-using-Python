### Time Complexity

The time complexity of the `isPalindrome` function is \( O(d) \), where \( d \) is the number of digits in the number \( x \).

**Explanation:**

-   The `while` loop iterates once for each digit in \( x \).
-   Each iteration performs a constant amount of work (extracting the last digit, updating the reversed number, and removing the last digit from \( x \)).
-   Thus, the number of iterations is proportional to the number of digits in \( x \), which gives the time complexity of \( O(d) \).

### Space Complexity

The space complexity of the `isPalindrome` function is \( O(1) \), or constant space.

**Explanation:**

-   The function uses a fixed amount of extra space:
    -   `initial`: stores the original number.
    -   `new_reversed_num`: accumulates the reversed number.
    -   `last_num`: temporarily holds the last digit of `x`.
-   These variables do not grow with the size of the input number; they only depend on a constant number of operations.
-   Therefore, the space complexity is constant, \( O(1) \).
