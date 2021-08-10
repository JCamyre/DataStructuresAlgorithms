# arr = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8]
# num = 3
# a = len(arr)
# k = 0
# for i in range(a):
#     if num != arr[i]:
#         k += 1
# print(k)

# def remove_element(nums: list, val: int):
#     a = len(nums)
#     k = 0
#     for i in range(a):
#         if val != nums[i]:
#             k += 1
#             x[]
            
#     return k

# class Solution:
#     def removeElement(self, xs, target_x):
#         non_garbage_index = 0

#         for x_i, x in enumerate(xs):
#             if x != target_x:
#                 xs[non_garbage_index], xs[x_i] = x, xs[non_garbage_index]
#                 non_garbage_index += 1

#         return non_garbage_index
    
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
            
def string_compression(s):
    if len(s) < 1:
        return s
    
    unique_chars = 0
    cur_char = s[0]
    cur_count = 0
    compressed_string = ''
    for char in s:
        if cur_char != char:
            compressed_string += cur_char + str(cur_count)
            cur_char = char
            unique_chars += 1
            cur_count = 0
        else:
            cur_count += 1
            
    if len(s)//3 + 1 < unique_chars:
        return s
    else:
        return compressed_string
    
print(string_compression('aabcccccaaa'))