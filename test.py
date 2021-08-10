arr = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8]
num = 3
a = len(arr)
k = 0
for i in range(a):
    if num != arr[i]:
        k += 1
print(k)

def remove_element(nums: list, val: int):
    a = len(nums)
    k = 0
    for i in range(a):
        if val != nums[i]:
            k += 1
            x[]
            
    return k

class Solution:
    def removeElement(self, xs, target_x):
        non_garbage_index = 0

        for x_i, x in enumerate(xs):
            if x != target_x:
                xs[non_garbage_index], xs[x_i] = x, xs[non_garbage_index]
                non_garbage_index += 1

        return non_garbage_index
    
    