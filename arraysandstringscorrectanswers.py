# 1.1 Time complexity O(n), n = length of string, since we are looping once through entire string once. The first if statement doesn't multiply n. 
# Space complexity O(1) since it is always 128 characters. Ik O(1) is constant space, but I always associated it with no space used lol. Technically time complexity O(1) too. 
# We are assuming only ASCII characters (128 unique characters)

def is_unique(s):
    # If more tha 128 characters, impossible for them all to be unique
    if len(s) > 128:
        return False
    
    # Have an array where each index represents a ascii code, all initially false. While looping through string, if an element is true, return False (it's a duplicate)
    chars = [False] * 128
    for char in s:
        ascii_code = ord(char)
        if chars[ascii_code]:
            return False
        chars[ascii_code] = True
        
    return True

# You could also just convert to set and compare len to the given string... but idk if interviewers would like that.

# 1.2
# Initial approach/brute force: O(n) space complexity: two hashmaps, see if they are equal. Just sort and compare. 
# Questions to clarify: case-sensitive? whitespace? Yes to both. 
# Obv observations: If the two strings have different lengths, they aren't permutations. (How do these optimizations affect runtime? Do we not change O(n), just say that it is more efficient?)
def are_permutations(s1, s2) -> bool:
    # Just sort and compare. Not bad. O(n logn) time, not sure for space complexity since sorted() usually needs some space. Can be improved.
    # if sorted(s1) == sorted(s2):
    #     return True
    # return False

    # Compare character counts. They use an array (I was thinking of a hashmap). Ig hashmap isn't answer to everything :(.
    # For C++/Java, need to know if ASCII or not to define the correct array size
    # I see a pattern (atleast in the first two problems) where they use an array where each index represents the corresponding ASCII code (ie i=99 represents 'c')
    
    # Real simple thing to improve optimization, can be used a lot.
    if len(s1) != len(s2):
        return False
    
    # Can increase size if extended ASCII
    arr = [0] * 128
    
    # Use array to represent the ascii codes. Store the frequency of each character in string1 by +1 in its respective index.
    for char in s1:
        arr[ord(char)] += 1
    
    # Compare to the characters in string2. -1 so that if strings are permutations, all elements are 0. Cancelling each other out.
    for char in s2:
        arr[ord(char)] -= 1
        
    if all(arr) == 0:
        return True
    return False

# 1.3
# Brute force/observations: All white-space within the length of the string is '%20'. Pythonic solution: '%20'.join(s[:length].split())
# I think I got bamboozled.
# Nah, I think it is just a weird problem for Java and maybe C++

# 1.4 Seems pretty obvious to just character count, as permutations means order doesn't matter, just that the characters are there.
# Do white-space matter? If not same length, then not permutation. Do lower-case matter? 
# I thought of the problem wrong... 
# What is a palindrome in term of character count? If even: all sets of 2. So can check a hashmap/array if all values are 0 or multiples of 2 (% 2) only. 
# Odd: Multiples of 3 and multiples of 2 only. well since white space counts... have to change a little. 
# So all multiples of 2 except for possible last one (odd) or last one + white space. If even, same amount of white space as single characters. 

def is_permutation_of_palindrome(s: str) -> bool:
    # Using hashmaps, may try arrays (using same concept of ASCII)
    s = s.lower()
    
    chars = {}
    for char in s:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
            
    print(chars)
    
    # tracks if any letter has only one, if so, return False
    # Kinda have to care about whitespaces
    odd = False
    for char in chars.keys():
        if chars[char] % 2 != 0 and char != ' ':
            if odd:
                return False
            odd = True
    # # of odds have to be equal to # of white-spaces. Have a white_spaces = 0. Every time if chars[char] % 2 != 0 and char != ' ': white_spaces -= 1. 
    return True

    # So I am right? They did it where they don't care about whitespace. 
    
    # One optimization, instead of checking for # of odd characters at the end, check as you are adding characters to hashmap. But, we have to run a few lines of code for each entry in hashmap, so maybe not more optimal. Talk to interviewer about it. 
    
    # High IQ bit manupulation. 
    
    

print(is_permutation_of_palindrome('Tact Coa'))

# 1.5
# Initial observations: Three conditions: insert a character -> length is one less, all matching characters between the two strings, except for one. 
# Remove a character -> All matching characters, except length is one more. Replace a character -> All matching characters except one.
# If all three conditions not true: Only one edit or less. 
# Can't use hashmap/array since order matters to store character frequency. 
# Bruteforce: O(n^2). If abs difference in length is greater than 1, return False. zipped for loop check if all characters equal, have a counter for number of differences
# Assumptions: White space matters, only lower case, 
# If s1 shorter, remove, s1 longer, add, equal, replace. Shift everything down one in the list. 


def one_away(s1: str, s2: str) -> bool:
    # Brute force O(n), n is length of shorter string since if strings were very different lengths, then the algorithm runs in O(1) (since it will auto return False). If they are about same length (<2), then n1 ~= n2.
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    # Change to boolean
    difference = True
    
    for i in range(min(len(s1), len(s2))): # Get's minimum range from two lists.
        if difference:
            return False 
        elif s1[i] != s2[i]:
            if len(s1) > len(s2):
                s1 = s1[1:]
            elif len(s2) > len(s1):
                s2 = s2[1:]
            difference = True
    return True

    # An optimization: check if difference_length == 1, if so, then we know removal or insert. 
    # Is my solution not optimal? Do I have to do i1 += 1, i2 += 1 indexes instead of lst = lst[:1]
    
    # Using while loop: 
    # If you aren't allowed to modify lists, do what they did with: while True: if difference: x1+=1 else: x1+=1, x2+=1
    
# 1.6 
# Brute force solutions: hashmap -> looping through keys + str(val). 
# Formula for determining if regular string shorter or equal to compressed: Need an average of Three characters. So... if len(s) // 3 + 1 < len(hashmap.keys()): return s
# So do we have to care about upper and lower case? 
# Should be able to take advantage of the array being sorted and have O(1) space. While looping through, until the cur element we care about changes, have a counter for the number of a specific element, and the total amount of unique characters. 

def string_compression(s):
    if len(s) < 1:
        return s
    
    # Bad name
    unique_chars = 1
    cur_count = 0
    compressed_string = ''
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            compressed_string += s[i] + str(cur_count)
            unique_chars += 1
            cur_count = 1
        else:
            cur_count += 1
    
    if s[-2] != s[-1]:
        compressed_string += s[-1] + 1
    else:
        compressed_string += s[-1] + len(cur_count)

    if len(s) < unique_chars * 2 + 1:
        return s
    else:
        return compressed_string
    # "It 's slow because string concatenation operates in O(n2) time"
    
    # You can check if the string has enough unique characters for it to be worth
    
    
