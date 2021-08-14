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

# Look at mario's solution?

# They split up their solutions/algorithms into a lot more functions than I do. I normally just have one main function. But they split up functions into many smaller functions (which is good for OOP). 

# One other benefit of this approach is that we can initialize StringBuilder to its necessary capacity
# up-front. Without this, StringBuilder will (behind the scenes) need to double its capacity every time it
# hits capacity. The capacity could be double what we ultimately need.

# OOP is programming "paradigm", keep everything as Class/objects (where you can have attributes linked to it) "allows you to package together data states and functionality to modify those data states"
# I need to use data states more, I like that word(s). As a result, code with OOP design is flexible, modular, and abstract.

# The 1.8 O(1) space solution so smart, using in-place and the first row and col to store the 0's. It's okay to modify the first row/col because once we come back to them, the entire row/col will be 0's.
