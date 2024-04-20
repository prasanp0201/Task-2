def remove_vowels(input_string):
    vowels = "aeiouAEIOU" # Define a string containing all vowels (both uppercase and lowercase)
    result_string = "".join(char for char in input_string if char not in vowels)
    return result_string
input_string = "Guvi Geeks Network Private Limited"
result = remove_vowels(input_string)
print("Original String:", input_string)
print("String with Vowels Removed:", result)