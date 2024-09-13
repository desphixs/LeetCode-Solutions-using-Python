def longestCommonPrefix(strs):
    # Define a function called longestCommonPrefix that takes a list of strings (strs) as input.
    
    if not strs: 
        # Check if the list of strings is empty.
        # If it is empty, there is no common prefix to find.
        return ""  # Return an empty string because there is no common prefix in an empty list.
    
    prefix = strs[0]
    # Initialize the prefix to be the first string in the list.
    # This is because the longest common prefix cannot be longer than the first string.

    for string in strs[1:]:
        # Loop through each string in the list starting from the second string.
        # This is done because we are comparing every string to the current prefix.
        
        while string[:len(prefix)] != prefix and prefix:
            # Inside the loop, compare the substring of the current string (up to the length of the prefix) with the prefix.
            # `string[:len(prefix)]` gives the beginning part of the current string of the same length as the prefix.
            # If this part of the current string does not match the prefix:
            
            prefix = prefix[:-1]
            # Remove the last character from the prefix.
            # This is done because the current prefix does not match the beginning of the string, so it needs to be shortened.
            # By removing one character from the end, we test a smaller prefix to see if it matches the current string.
            
        # If `prefix` becomes empty, it means there is no common prefix and the loop will exit.

    return prefix
    # After all strings have been processed, return the remaining `prefix`.
    # This is the longest common prefix shared by all strings in the list.

strs = ["flower","flow","flight"]
# Define a list of strings to test the function.

print(longestCommonPrefix(strs))
# Call the longestCommonPrefix function with the list `strs` and print the result.
# This will show the longest common prefix shared by the strings in the list.



# Solved 11th September, 2024
# Destiny Franks