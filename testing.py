# class SingleLinkedNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
        
#     def __str__(self):
#         return str(self.val)
        
# def reverse(head):
#     cur_node = head
#     prev = None
#     while cur_node.next:
#         next = cur_node.next
#         cur_node.next = prev
#         prev = cur_node
#         cur_node = next
#     # This is example of special case, tail of linkedlist.
#     cur_node.next = prev
#     return cur_node

# head = SingleLinkedNode(5)
# cur_node = head
# for i in range(4, 0, -1):
#     cur_node.next = SingleLinkedNode(i)
#     cur_node = cur_node.next

# tail = reverse(head)
# print(tail, tail.next)
# while tail.next:
#     print(tail)
#     tail = tail.next
# print(tail)


arr = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
n = len(arr) # Since assuming a square


def display_grid(arr):
    for j in arr:
        print('  '.join([str(i) for i in j]), end='\n' * 2)
display_grid(arr)     
print('*' * 40)

from math import ceil

for j in range(ceil(n/2)):
    first = j
    last = n - j - 1
    if first >= last:
        print('DONE')
    for i in range(first, last):
        # Have one value as a constant so that you can perform the 90 degree shift.
        # Temp left
        offset = i - first
        # top
        temp = arr[last-offset][first]
        print(temp)
        arr[first][i], temp = temp, arr[first][i]
        print(temp)
        # right
        arr[i][last], temp = temp, arr[i][last]
        print(temp)
        # bottom 
        arr[last][last-offset], temp = temp, arr[last][last-offset]
        print(temp)
        # left
        arr[last-offset][first], temp = temp, arr[last][last-offset]
        print(temp)
        
        display_grid(arr)
        print('*' * 40)


        
display_grid(arr)