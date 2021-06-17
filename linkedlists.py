from os import extsep


class SingleLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
# 1.1 Brute force: loop through linkedlist, store values in hashtable, if in hashtable, delete node (O(N) time, O(N) space). w/O USING temporary buffers, use two pointers. O(N^2)
def remove_dups(head: SingleLinkedNode):
    if not head or not head.next:
        return head
        
    # hashmap = {}
    # cur_node = head
    # prev_node = None
    # while cur_node.next:
    #     print(cur_node.val)
    #     if cur_node.val in hashmap:
    #         print('Copy:', cur_node.val)
    #         prev_node.next = cur_node.next 
    #     else:
    #         hashmap[cur_node.val] = cur_node.val
    #     prev_node = cur_node
    #     cur_node = cur_node.next 
    
    # if cur_node.val in hashmap:
    #     prev_node.next = None 
    # else:
    #     hashmap[cur_node.val] = cur_node.val
    cur = head
    while cur.next:
        prev_node = None
        p1 = cur
        # If p1 is third node, once we reach end of linkedlist, we have to go back and compare first and second node
        p2 = head
        while p2.next:
            if p1 != p2 and p1.val == p2.val: # if they aren't the exact same node object but their values are the same
                print(p2.val)
                prev_node.next = p2.next.next
                p2 = prev_node.next.next
            else:
                prev_node = p2        
                p2 = p2.next 
        cur = cur.next
                            
    
    return head


cur = SingleLinkedNode(0)
head = cur
for i in range(1, 10):
    cur.next = SingleLinkedNode(i)
    cur = cur.next

for i in range(0, 10, 3):
    cur.next = SingleLinkedNode(i)
    cur = cur.next

remove_dups(head)
    
# 1.2 use two pointers (fast pointer is kth elements ahead of slow pointer, have to have check to ensure no error)
def kthtolast(head, k):
    p1 = head
    p2 = head
    i = 0 
    for i in range(k):
        if p2.next:
            p2 = p2.next
        else:
            return "Linkedlist too short!"    
    while i != k and p2.next:
        p1 = p1.next 
        p2 = p2.next
    # Returning kth element from the end 
    return p1
        
# 1.3