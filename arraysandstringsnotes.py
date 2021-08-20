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


# 1.2, comparing permutations between two strings, array for characters (128 for ASCII), add values to array for s1, remove values to s2, if all values 0, then equal

# 1.4 checking for palindrome general concept: all even values except for a max of one character that has one occurence. 
# Ex: {'a': 4, 'b': 2, 'c': 1} is a palindrome. {'a': 4, 'b': 2, 'c': 1, 'd': 1} is not a palindrome.

# 1.5 Check if insert/removal and/or replace. Basically iterating through both strings, comparing, if difference, which ever longer do x1+=1 or x2+=1 only. 
# Instead of x1+=1 and x2+=1. Using while loops and x1+=1/x2+=1 interesting when comparing strings

# 1.6 Split up algo into a lot of functions

# 1.7 Had a good time with this one :))). Think of matrix as layers, and loop layers until half way of matrix height/width. A lot easier to explain with an illustration.
# The replacement thing pretty interesting. Have to save the element from "top" layer. Then go about replacing the bot value with the right value, left value with bot value, top value with left value, and right value with the saved top value. 
# For many different algorithms, storing an initial value before you change in place very important.

# Side note, inverting binary tree so easy. Reversing linked lists takes 4 lines in the while loop (optional if statement)

# 1.8 O(1) space solution so smart, using in-place and the first row and col to store the 0's. It's okay to modify the first row/col because once we come back to them, the entire row/col will be 0's.
# So genius way to change in place part of the data structure to keep track of how to change in place the rest of it. Very interesting. These O(1) space solutions r cracked

# 1.9 Very, very simple solution. Just pure logic/thinking: if s2 is a rotation of s1, then there is a rotation point, where s1 = x + y, and s2 = y + x. 
# Ex: s1 = 'birthday' = 'birth' + 'day', s2 = 'daybirth' = 'day' + 'birth'
# Therefore, s2s2 = y(xy)x, s1(xy) MUST be in s2s2 for them to be rotations of each other. Then just put isSubString(s2s2, s1)

# General tips
# Using two pointers, or more
# Sliding window
# Principles specific to a problem: https://leetcode.com/problems/container-with-most-water/. Min/maxing height vs width. Taking the smallest trade off possible (one width for the smallest of the two line)
# Use max(area, max_area) instead of if area > max_area: 
# Instead of doing a triple nested loop, do one for loop, then for the other two pointers, 
# O(n^2) instead of O(n^3). 
# Sometimes is using a sorting algorithm worth? Makes a lot more efficient: "set values and do j+=1 or k-=1 depending on new_value compared to target value"
# Without sorting array can't do 1 for loop + while loop. num.sort(), num = sorted(num)
