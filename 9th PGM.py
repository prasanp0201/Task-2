def count_words(input_string):
    words_list = input_string.split()     # Split the input string into words based on whitespace
    return len(words_list) # Return the length of the words list, which gives the count of words
input_string = "Eva, can I see bees in a cave"
word_count = count_words(input_string)
print("Number of Words:", word_count)