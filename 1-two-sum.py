
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store seen values and their indices
        seen = {}

        # Loop through each number and its index in the input list
        for index, value in enumerate(nums):
            # Calculate the value needed to reach the target
            pair_value = target - value
            
            # Check if the needed value is in the seen dictionary
            if pair_value in seen:
                # If found, return the indices of the two numbers that sum up to the target
                return [seen[pair_value], index]
            
            # If not found, add the current value and its index to the seen dictionary
            seen[value] = index



# Create an instance of the Solution class
solution_instance = Solution()

# Define the input list of integers (nums) and the target integer (target)
nums = [2, 7, 11, 15]
target = 17

# Call the twoSum method with the defined nums list and target
result = solution_instance.twoSum(nums, target)
print("Indices of the two numbers that sum up to the target:", result)


# Tutorial URL
# Coming Soon