#Python program that takes a string and returns true if it is an anagram of another string, false otherwise

def is_anagram(str1, str2):
    # Remove spaces and convert strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)     # Check if the sorted versions of the strings are equal
string1 = "typhon"
string2 = "python"
result = is_anagram(string1, string2)
print("Are '{}' and '{}' anagrams?".format(string1, string2), result)