#Python program to calculate total number of vowels and count of each individual vowel A, E, I, O, U in the string "Guvi Geeks Network Private Limited"

def count_vowels(string):
    string = string.lower() # Convert the string to lowercase to handle both uppercase and lowercase vowels
    
    # Initializing variables to store counts of each vowel
    total_vowels = 0
    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0

    for char in string: # Iterate through each character in the string
        if char in 'aeiou': # Check if the character is a vowel
            total_vowels += 1  # Increment total vowels count

            # Increment individual vowel counts based on the vowel encountered
            if char == 'a':
                count_a += 1
            elif char == 'e':
                count_e += 1
            elif char == 'i':
                count_i += 1
            elif char == 'o':
                count_o += 1
            elif char == 'u':
                count_u += 1

    return total_vowels, count_a, count_e, count_i, count_o, count_u # Return the total vowels count and counts of individual vowels

input_string = "Guvi Geeks Network Private Limited"
total_vowels, count_a, count_e, count_i, count_o, count_u = count_vowels(input_string)

print("Total vowels:", total_vowels)
print("Count of 'A':", count_a)
print("Count of 'E':", count_e)
print("Count of 'I':", count_i)
print("Count of 'O':", count_o)
print("Count of 'U':", count_u)