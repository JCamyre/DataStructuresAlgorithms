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

def removeElement(xs, target_x):
    non_garbage_index = 0

    for x_i, x in enumerate(xs):
        if x != target_x:
            xs[non_garbage_index], xs[x_i] = x, xs[non_garbage_index]
            non_garbage_index += 1

    return non_garbage_index, xs

# print(removeElement([1, 2, 2, 3], 2))
    
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
        compressed_string += s[-1] + str(1)
    else:
        compressed_string += s[-1] + str(cur_count)

    if len(s) < unique_chars * 2 + 1:
        return s
    else:
        return compressed_string
    # "It 's slow because string concatenation operates in O(n2) time"
    
    # You can check if the string has enough unique characters for it to be worth
    
# print(string_compression('aabbcc'))

# arr[j][i] = arr[i][max-j]
# Top left (j > len(arr[j]) // 2 and i < len(arr[i]) // 2) and bottom right x () value change, bottom left and top right y value change
# So what about the halfway point?
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
if not len(arr) > 1 and not len(arr[0]) > 1:
    print(arr)
    
    
for j in range(len(arr)):
    for i in range(len(arr[0])):
        print(i, j)
        if (j <= len(arr[j])//2 and i <= len(arr[i]) // 2) or (j > len(arr[j])//2 and i > len(arr[i]) // 2):
            print(abs(i-len(arr[:-1])))
            arr[j][abs(i-len(arr[0][:-1]))] = arr[j][i] 
        else:
            arr[j-abs(j-len(arr[:-1]))][i] = arr[j][i]
        
def display_grid(arr):
    for j in arr:
        print('  '.join([str(i) for i in j]), end='\n' * 2)

display_grid(arr)

if len(arr) < 1 or len(arr) != len(arr[0]):
    print('BAD')
n = len(arr) # Since assuming a square
# left -> top, top -> right, right -> bottom, bottom -> left
# Do layers until halfway point
for j in range(n//2):
    first = j
    last = n - j - 1
    for i in range(first, last):
        # Have one value as a constant so that you can perform the 90 degree shift.
        # Temp left
        print(arr, i, arr[i][last])
             
        # top
        temp = arr[i][first]
        arr[i][first], temp = temp, arr[first][i]
        
        # right
        arr[i][last], temp = temp, arr[i][last]
        
        # bottom 
        arr[last][i], temp = temp, arr[last][i]
        
        # left
        arr[first][i], temp = temp, arr[first][i]
        
display_grid(arr)
        
