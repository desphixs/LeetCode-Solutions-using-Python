def isPalindrome(x):
    if x < 0:
        return False

    initial = x
    new_reversed_num = 0

    while x > 0:
        """
        This line extracts the last digit of x.
        Example: if x is 305, last_num = 305 % 10 = 5
        """
        last_num = x % 10 

        """
        This line updates the reversed number by shifting the previous digits left and adding the new last_num.
        Example: if new_reversed_num is 0, it becomes 0 * 10 + 5 = 5
        """
        new_reversed_num = new_reversed_num * 10 + last_num 

        """
        This line removes the last digit from x.
        Example: if x is 305, x becomes 305 // 10 = 30
        """
        x //= 10

    # Return True if the reversed number matches the initial number, else return False
    return new_reversed_num == initial

print(isPalindrome(1234))  # Output will be False
print(isPalindrome(-121))  # Output will be True




"""
The lines `new_reversed_num = new_reversed_num * 10 + last_num` and `x = x // 10` work together to reverse the digits of a number. Here's how each line contributes to this process:

### Reversing the Number

1. **Extracting the Last Digit (`last_num = x % 10`)**:
   - `last_num` gets the last last_num of `x`. For example, if `x` is `1234`, `last_num` will be `4` (from `1234 % 10`).

2. **Building the Reversed Number (`new_reversed_num = new_reversed_num * 10 + last_num`)**:
   - This line updates `new_reversed_num` by shifting its current digits left and adding the new last_num at the end.
   - **Initialization**: Initially, `new_reversed_num` is `0`.
   - **First Iteration**: 
     - Suppose `last_num` is `4`. `new_reversed_num` is updated to `0 * 10 + 4` = `4`.
   - **Second Iteration**: 
     - Now if `last_num` is `3`, `new_reversed_num` was `4`. Update it to `4 * 10 + 3` = `43`.
   - This process continues, shifting `new_reversed_num` left and adding each new last_num from `x`.

3. **Removing the Last Digit from `x` (`x = x // 10`)**:
   - This line removes the last last_num from `x`.
   - **First Iteration**:
     - For `x = 1234`, after extracting `4`, `x` is updated to `1234 // 10` = `123`.
   - **Second Iteration**:
     - After extracting `3`, `x` is updated to `123 // 10` = `12`.
   - This process continues until `x` is reduced to `0`, leaving `new_reversed_num` containing the digits in reverse order.

### Example:

Consider `x = 1234`:

1. **Initial Values**:
   - `new_reversed_num = 0`
   - `x = 1234`

2. **Iteration 1**:
   - `last_num = 1234 % 10` = `4`
   - Update `new_reversed_num`: `new_reversed_num = 0 * 10 + 4` = `4`
   - Update `x`: `x = 1234 // 10` = `123`

3. **Iteration 2**:
   - `last_num = 123 % 10` = `3`
   - Update `new_reversed_num`: `new_reversed_num = 4 * 10 + 3` = `43`
   - Update `x`: `x = 123 // 10` = `12`

4. **Iteration 3**:
   - `last_num = 12 % 10` = `2`
   - Update `new_reversed_num`: `new_reversed_num = 43 * 10 + 2` = `432`
   - Update `x`: `x = 12 // 10` = `1`

5. **Iteration 4**:
   - `last_num = 1 % 10` = `1`
   - Update `new_reversed_num`: `new_reversed_num = 432 * 10 + 1` = `4321`
   - Update `x`: `x = 1 // 10` = `0`

6. **Final Values**:
   - `new_reversed_num = 4321`
   - `x = 0` (loop terminates)

The final value of `new_reversed_num` is `4321`, which is the reverse of `1234`.

### Summary:

- **`new_reversed_num = new_reversed_num * 10 + last_num`**: This line builds the reversed number by appending the last last_num of `x` to `new_reversed_num`.
- **`x = x // 10`**: This line removes the last last_num from `x`, preparing for the next iteration to extract and process the new last last_num.

Together, these lines reverse the digits of `x` through iterative extraction and construction.
"""


# Solved 11th September, 2024
# Destiny Franks