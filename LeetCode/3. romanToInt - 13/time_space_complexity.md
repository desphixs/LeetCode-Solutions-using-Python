### Time Complexity:

The time complexity of the `romanToInt` function is **O(n)**, where **n** is the length of the input string `s`.

-   **Why O(n)?**: The function loops through each character of the Roman numeral string once, performing constant-time operations (comparisons, dictionary lookups, addition, or subtraction). The loop runs for **n-1** iterations, and the final addition of the last character takes constant time. Thus, the overall time complexity is linear in relation to the length of the string.

### Space Complexty:

The space complexity is **O(1)** (constant space).

-   **Why O(1)?**: The function uses a fixed dictionary to map Roman numerals to integers, and a few integer variables (`total` and the loop counter). No additional data structures are used that scale with the size of the input string. Even though the input string has length `n`, the function only processes one character at a time, so it doesn’t require extra space that depends on the size of the input.

### Lets quickly simmarize it:

-   **Time Complexity**: O(n) (linear with respect to the length of the Roman numeral string)
-   **Space Complexity**: O(1) (constant space, regardless of input size)
