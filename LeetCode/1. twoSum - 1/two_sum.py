def twoSum(nums, target):
    """
    Finds two numbers in the list `nums` that add up to the `target` sum.
    Returns the indices of these two numbers.

    Args:
    nums (list of int): List of integers.
    target (int): Target sum to find.

    Returns:
    list of int: Indices of the two numbers that add up to `target`.

    Example:
    >>> nums = [2, 7, 11, 15]
    >>> target = 9
    >>> twoSum(nums, target)
    [1, 0]
    """
    # Initialize an empty dictionary to store the numbers and their indices
    number_dict = {}

    # Iterate over the list `nums` with index and value
    for index, value in enumerate(nums):
        """
        Calculate the difference needed to reach the target sum
        For each number in nums, the code calculates the diff (difference) between the target and the current value. 
        This is essentially asking: "What number would I need to add to this value to get the target?"
        """
        diff = target - value

        # Check if the difference is already in the dictionary
        if diff in number_dict:
            # If found, return the indices of the two numbers
            return [index, number_dict[diff]]
        else:
            # If not found, store the current number and its index in the dictionary
            number_dict[value] = index

# Define a list of numbers and a target value
nums = [2, 7, 11, 15]

# Call the twoSum function with the list and target, and store the result
result = twoSum(nums, 9)

# Print the result to the console
print(result)




# Solved 11th September, 2024
# Destiny Franks