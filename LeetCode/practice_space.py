# Define the Solution class
class Solution(object):
    # Define the method 'isValid' that takes a string 's' as input
    def isValid(self, s):
        # Initialize an empty list to use as a stack for tracking opening brackets
        stack = []
        
        # Iterate over each character in the input string
        for i in s:
            # If the character is one of the opening brackets
            if i in "({[":  
                # Push the opening bracket onto the stack
                stack.append(i)
            # If the character is one of the closing brackets
            elif i in ")}]":  
                # Check if the stack is empty (i.e., no matching opening bracket)
                if not stack:
                    # If the stack is empty, it means there is no matching opening bracket
                    return False
                # If the character is a closing bracket, check if it matches the top of the stack
                if i == ")" and stack[-1] == "(":
                    # If it matches, pop the top of the stack (i.e., remove the matching opening bracket)
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    # If it matches, pop the top of the stack
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    # If it matches, pop the top of the stack
                    stack.pop()
                else:
                    # If the closing bracket does not match the top of the stack, return False
                    return False
        
        # After processing all characters, return True if the stack is empty (all brackets matched)
        # Return False if the stack is not empty (some opening brackets did not have matching closing brackets)
        return not stack

# This block of code runs only if the file is executed directly, not if imported as a module
if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    # Define a list of test strings to check the validity of bracket sequences
    test_strings = ["[()]", "({[]})", "([)]", "", "((()))", "{[()()]}", "{[", "([])"]
    # Iterate over each test string
    for s in test_strings:
        # Call the isValid method on the current test string and print the result
        # The output will be in the format: isValid(test_string): result
        print(f"isValid({s}): {sol.isValid(s)}")
