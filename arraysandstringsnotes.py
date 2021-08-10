# The use of the array where each index represents the ASCII code is genius (cleaner than hashmap in some cases). Each element represents the frequency of correspondiong character, or could be boolean representing if character present in string.

# Other tricks/small optimizations: 

# Using bits/bit manupulation :flushed:. For the palindrome problem, only 26 possible characters. For an 8 bit integer, can store any char. For the frequencies, if only one, add one to the corresponding bit. By the end, if the 8 bit integer/bit vector != 0, odd # of char. 
# Better explanation: "Toggle" the bits. For the even # of chars, the bit vector would remain zero. But if an odd # of chars, the value would remain, thus != 0.
# I.e: 'a' is 0 (which is 0 in binary), 'c' is 2(10 in binary), etc. If there are two 'a's and two 'c's, then the final int should be zero. 
# Ig I need to learn more about bit manipulation
# A note for bit manipulation: you are supposed to perform bit operations with the integer. bin() converts to a string
# I NEED TO COMEBACK TO THIS, NOT TOTALLY SURE HOW TO DO IN PYTHON.
# for (char c : phrase.toCharArray(» { int x = getCharNumber(c); HMMMM. If we can use space, a hashmap or array ['a', 'b', 'c', ...] and do array.index('a') as the integer value.

# Simple solution with Python, but idk if interviewers want to see this.
from collections import Counter
def is_palindrome_permutation_pythonic(phrase):
    """function checks if a string is a permutation of a palindrome or not"""
    counter = Counter(phrase.replace(" ", "").lower())
    return sum(val % 2 for val in counter.values()) <= 1

# Many different tricks, some only for lower-level languages like Java/C++