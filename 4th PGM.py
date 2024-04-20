#Python program that takes a string and returns the number of uniques characters in it

def count_unique_characters(input_string):
    unique_chars = set(input_string) # Create a set to store unique characters
    return len(unique_chars) # Return the length of the set, which gives the count of unique characters
input_string = "MS Dhoni is the best finisher in world cricket"
unique_count = count_unique_characters(input_string)
print("Number of Unique Characters:", unique_count)