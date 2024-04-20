#Python program that takes a string and returns true if it is a palindrome, false otherwise

def is_palindrome(input_string):
    processed_string = input_string.lower().replace(" ", "") # Convert the input string to lowercase and remove spaces
    return processed_string == processed_string[::-1]     # Check if the processed string is equal to its reverse
input_string = "He lived as a devil eh"
result = is_palindrome(input_string)
print("Is Palindrome:", result)