The `romanToInt` function is designed to convert a Roman numeral string into an integer. Let's break it down step by step so you can understand how it works, especially as a beginner in Data Structures and Algorithms (DSA).

### Roman Numeral Basics

Roman numerals have specific values:

-   **I = 1**
-   **V = 5**
-   **X = 10**
-   **L = 50**
-   **C = 100**
-   **D = 500**
-   **M = 1000**

Roman numerals are typically written from largest to smallest, left to right. However, when a smaller numeral appears before a larger one, it means you subtract the smaller value. For example:

-   **IV = 4** (5 - 1)
-   **IX = 9** (10 - 1)

### Code Breakdown

```python
def romanToInt(self, s):
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
```

Here, we create a dictionary `roman` that maps each Roman numeral character to its integer value. This dictionary is our reference to look up the value of each numeral in the input string.

### Step 1: Initialize the Total

```python
    total = 0
```

The `total` variable will hold the final integer value of the Roman numeral string as we process each character.

### Step 2: Iterate Through the String

```python
    for i in range(len(s) - 1):
```

The loop goes through the string from the first character to the second-to-last character (`len(s) - 1`). This is because the loop compares each character to the next one, so we don’t need to compare the last character with anything (we handle the last character separately later).

### Step 3: Compare Adjacent Numerals

```python
        if roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
```

This is the core logic for converting Roman numerals to integers.

-   **If the current numeral is smaller than the next numeral**, it means we need to subtract its value. For example, in **"IV"**, since **I (1)** is less than **V (5)**, we subtract **1** from the total.
-   **Otherwise, we add the current numeral’s value to the total**. For example, in **"VI"**, since **V (5)** is greater than **I (1)**, we add **5** and then add **1**.

### Step 4: Add the Last Character

```python
    return total + roman[s[-1]]
```

At the end, we add the value of the last character (`s[-1]`) to the total. The reason the last character is handled separately is that there’s no next character to compare it to in the loop.

### Example Walkthrough

Let’s use the input **"XIV"** (which is **14**) as an example:

1. **roman["X"] = 10**, **roman["I"] = 1**, **roman["V"] = 5**.
2. In the first loop iteration, we compare **X** (10) and **I** (1). Since 10 is greater than 1, we add 10 to `total` (total = 10).
3. In the second loop iteration, we compare **I** (1) and **V** (5). Since 1 is less than 5, we subtract 1 from `total` (total = 9).
4. After the loop, we add the value of the last character **V** (5) to the `total`. So the final result is **9 + 5 = 14**.

### Time Complexity

-   The time complexity of this algorithm is **O(n)**, where **n** is the length of the string `s`. We traverse each character of the string exactly once, performing constant-time operations (comparisons and lookups).

### Key Points to Understand

1. **Roman numeral subtraction rule**: This is the trickiest part for beginners. If a smaller numeral is followed by a larger numeral, we subtract instead of adding.
2. **Efficient use of a dictionary**: Dictionaries in Python allow for quick lookups (O(1) time complexity), making the algorithm efficient.
3. **Final addition for the last numeral**: Since we loop only up to the second-to-last character, we add the last character’s value after the loop to ensure we account for it.

This solution efficiently handles the conversion using a simple loop and some conditional logic!
