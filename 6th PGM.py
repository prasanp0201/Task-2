#Python program that takes two strings and returns the longest common substring between them

def longest_common_substring(str1, str2):
    # Initialize variables to store the length and starting index of the longest common substring
    max_length = 0
    start_index = 0
    matrix = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]     # Create a matrix to store the lengths of common substrings
    for i in range(1, len(str1) + 1): # Iterate over the characters of both strings
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
                if matrix[i][j] > max_length:
                    max_length = matrix[i][j]
                    start_index = i - max_length
    return str1[start_index:start_index + max_length] # Return the longest common substring
string1 = "Sachin Tendulkar"
string2 = "Rachin Ravindra"
common_substring = longest_common_substring(string1, string2)
print("Longest Common Substring:", common_substring)