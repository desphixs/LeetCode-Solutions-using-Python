1. **Function Definition**:

    ```python
    def isPalindrome(x):
    ```

    - Defines a function `isPalindrome` that checks if the number `x` is a palindrome.

2. **Negative Check**:

    ```python
    if x < 0:
        return False
    ```

    - Checks if the number is negative. Negative numbers cannot be palindromes, so it immediately returns `False` if `x` is less than `0`.

3. **Initialize Variables**:

    ```python
    initial = x
    new_reversed_num = 0
    ```

    - Stores the original number `x` in `initial`.
    - Initializes `new_reversed_num` to `0`, which will be used to build the reversed number.

4. **Reverse the Number**:

    ```python
    while x > 0:
        last_num = x % 10
        new_reversed_num = new_reversed_num * 10 + last_num
        x //= 10
    ```

    - **Extract Last Digit**:
        ```python
        last_num = x % 10
        ```
        - Gets the last digit of `x` using the modulus operator (`%`).
    - **Update Reversed Number**:
        ```python
        new_reversed_num = new_reversed_num * 10 + last_num
        ```
        - Shifts the current digits of `new_reversed_num` left by multiplying it by `10` and adds the last digit (`last_num`) to it.
    - **Remove Last Digit from `x`**:
        ```python
        x //= 10
        ```
        - Removes the last digit from `x` by performing integer division (`//`).

5. **Return Result**:

    ```python
    return new_reversed_num == initial
    ```

    - Compares the reversed number (`new_reversed_num`) with the original number (`initial`). Returns `True` if they are equal, indicating that `x` is a palindrome; otherwise, it returns `False`.

6. **Function Calls**:
    ```python
    print(isPalindrome(1234))  # Output will be False
    print(isPalindrome(-121))  # Output will be False
    ```
    - Calls the `isPalindrome` function with test values `1234` and `-121`, printing the results. Both should return `False` because neither is a palindrome.
