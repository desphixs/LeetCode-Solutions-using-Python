def romanToInt(s):
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total + roman[s[-1]]

print(romanToInt("XIX"))




"""
## Analyzing the LeetCode Question: Roman to Integer

**Understanding the Problem:**

1. **Input:** A Roman numeral string.
2. **Output:** The equivalent integer value.
3. **Rules:**
   - Roman numerals are represented by seven symbols with specific values.
   - Numbers are generally written from largest to smallest.
   - Subtraction is used for certain combinations (e.g., IV, IX).

**Initial Thinking Process:**

1. **Data Structure:**
   - Given the input is a string, a suitable data structure would be a string or an array of characters.

2. **Approach:**
   - **Iterative:** Traverse the string from left to right, keeping track of the current value and comparing it with the next character. If the next character represents a larger value, subtract the current value; otherwise, add it.
   - **Hash Table:** Create a hash table mapping Roman numerals to their corresponding integer values. Iterate through the string, looking up the values in the hash table and applying the subtraction rule as needed.

3. **Edge Cases:**
   - **Empty string:** Return 0.
   - **Invalid Roman numerals:** Handle cases like "IIII" or "VV".
   - **Large numbers:** Consider the range of integers that can be represented.

**Method Choice:**

The iterative approach is generally more intuitive for this problem. It involves a straightforward traversal and conditional logic to handle the subtraction rule. However, if you're comfortable with hash tables and prefer a more concise solution, you could use that approach.

**Key Points:**

- **Subtraction rule:** Understand the specific combinations that require subtraction.
- **Edge cases:** Consider potential invalid inputs or extreme values.
- **Clarity:** Choose an approach that is easy to understand and implement.

By following these steps, you can effectively analyze the problem and develop a suitable solution.

"""