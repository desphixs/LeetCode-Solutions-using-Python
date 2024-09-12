def romanToInt(s):
    # Map Roman numeral symbols to their corresponding integer values in a dictionary
    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    # Initialize total to store the sum of converted Roman numerals
    total = 0

    """
    Loop through the string, processing each Roman numeral except for the last character.
    We stop at the second-to-last character because in each iteration, we compare the current
    numeral with the next one. The last character has no next value to compare against, so it will
    be handled separately after the loop.
    """
    for i in range(len(s) - 1):
        """
        If the value of the current Roman numeral (s[i]) is smaller than the next one (s[i+1]),
        it indicates a subtractive pair (e.g., "IV" or "IX"). In that case, subtract the value of the
        current numeral from the total.
        """
        if roman[s[i]] < roman[s[i + 1]]:
            # Subtract the value of the current Roman numeral from total
            total -= roman[s[i]]
        else:
            """
            If the current Roman numeral (s[i]) is greater than or equal to the next one (s[i+1]),
            we add its value to the total. This handles the usual left-to-right additive cases (e.g., "VI" or "XII").
            """
            total += roman[s[i]]

    """
    Finally, add the value of the last Roman numeral (s[-1]) to the total. Since it was excluded
    from the loop, we handle it separately here.
    """
    return total + roman[s[-1]]

# Example: Testing the function with the Roman numeral "XIX" (which equals 19)
print(romanToInt("XIX"))


# Solved 12th September, 2024
# Destiny Franks