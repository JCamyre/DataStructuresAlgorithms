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
    # # of odds have to be equal to # of white-spaces
    return True

    # So I am right? They did it where they don't care about whitespace. 
    

print(is_permutation_of_palindrome('Tact Coa'))

