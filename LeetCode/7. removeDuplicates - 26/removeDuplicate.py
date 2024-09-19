class Solution(object):
    def removeDuplicates(self, nums):
        # Initialize pointer 'j' to 0, which will track the position for the next unique element.
        j = 0

        # Iterate through the array starting from the second element (index 1).
        for i in range(1, len(nums)):
            # Compare the current element with the element at index 'j'.
            # If they are different, it means nums[i] is a new unique element.
            if nums[i] != nums[j]:
                # Increment 'j' to move to the next position for the new unique element.
                j += 1
                # Place the current unique element (nums[i]) at the new position 'j'.
                nums[j] = nums[i]

        # Return the number of unique elements, which is 'j + 1'.
        # 'j' is the index of the last unique element, so the count of unique elements is 'j + 1'.
        # return j + 1

# Example usage
nums = [1, 1, 2]
sol = Solution()
# Print the result of removeDuplicates function, which is the count of unique elements.
print(sol.removeDuplicates(nums))



"""
Explanation:
Initialization of j: j = 0 sets up the pointer to track the position of the last unique element. Initially, the first element is considered unique, so j starts at 0.

Loop from index 1: for i in range(1, len(nums)) iterates through the array starting from the second element (index 1). The first element is already considered unique, so we start checking from the second element.

Check for uniqueness: if nums[i] != nums[j] checks if the current element (nums[i]) is different from the last unique element (nums[j]). If they are different, nums[i] is a new unique element.

Update j and nums[j]:

j += 1 moves the j pointer to the next position.
nums[j] = nums[i] places the new unique element at the updated position j.
Return the count of unique elements: return j + 1 returns the count of unique elements. j is the index of the last unique element, so adding 1 gives the total number of unique elements.

Example usage: The example creates a Solution object and tests the removeDuplicates function with a sample input. It prints the number of unique elements returned by the function.

"""