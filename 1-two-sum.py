
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



'''
Question 1: Is it necessary and compulsory to add these parameters in the function?

Answer: In Python, it's not necessary to explicitly include self as the first parameter in methods if they don't access instance attributes or methods. However, if you're defining a method within a class and plan to call it on instances of that class, it's a common convention to include self as the first parameter to represent the instance itself.

Regarding the type hints (nums: List[int], target: int) and return type hint (-> List[int]), they are optional but can be helpful for documenting and enforcing types in your code. They improve readability and can catch type-related errors early during development. If you're using type hints, it's a good practice to be consistent throughout your codebase.

Here's a breakdown of the parameters and return type hint in the context of your method signature:

nums: List[int]: This indicates that the nums parameter is expected to be a list of integers. The List[int] part is a type hint provided by the typing module, specifying that nums should be a list where each element is an integer.

target: int: This indicates that the target parameter is expected to be an integer. The int part is a type hint specifying the type of the target parameter.

-> List[int]: This indicates that the method is expected to return a list of integers. The -> List[int] part is a return type hint specifying the type of the return value.
'''