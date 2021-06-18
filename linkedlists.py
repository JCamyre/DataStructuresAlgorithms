from os import extsep


class SingleLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __str__(self):
        return str(self.val)
        
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
        
# 2.3 Solution very simple, I was overthinking. The current node is still linked to the prev node, but we are replacing the val and next so that it impersonates/replaces the next node.

def delete_middle_node(node):
    node.val = node.next.val
    node.next = node.next.next

# def recursive(head):
#     if head.next:
#         recursive(head.next)
#     else:
#         return head

# 2.4 Sorta sorting, but not really. Traverse through linkedlist, if less than val, put it as head (node.next = head), otherwise, but it as tail. 
def partition(head, x):
    mid = head
    cur_head = head
    cur = head.next
    while cur.next:
        if cur.val < x:
            # inserting new head
            cur.next = cur_head
            cur_head = cur
        else:
            # insertion
            mid.next.next = mid.next
            mid.next = cur
    
    return cur_head
        
# 2.5 I'll admit it, I've done this problem before. The reversed linked list is good, since this is how we add numbers normally (smallest place to largest).
def sum_lists(head1: SingleLinkedNode, head2: SingleLinkedNode):
    # Doesn't say to assume linkedlists are same length
    # Idea: instead of creating third linkedlist for output, just update values of cur1
    # Special case: linkedlists are not same length
    cur1 = head1
    cur2 = head2
    # output = None
    carry = 0
    place = 0
    head = cur1
    while cur1.next and cur2.next:
        
        sum = cur1.val + cur2.val 
        place = sum % 10
        cur1.val = place + carry
        
        carry = sum // 10 
        cur1 = cur1.next
        cur2 = cur2.next
        # if output:
        #     output.next = SingleLinkedNode(sum)
        #     output = output.next
        # else:
        #     output = SingleLinkedNode(sum)
    if cur1.next:
        while cur1.next:
            cur1.val += carry
    elif cur2.next:
        while cur2.next:
            cur2.val += carry
    else:
        sum = cur1.val + cur2.val 
        place = sum % 10
        cur1.val = place + carry
    
    return head

# 7 1 6
head1 = SingleLinkedNode(7)
head1.next = SingleLinkedNode(1)
head1.next.next = SingleLinkedNode(6)

head2 = SingleLinkedNode(5)
head2.next = SingleLinkedNode(9)
head2.next.next = SingleLinkedNode(2)
            
head = sum_lists(head1, head2)
while head.next:
    print(head)
    head = head.next
print(head)

# 2.6 Two pointers. Two ways: Constant space with the "runner technique". O(N) space if we use runner technique and a stack (where first in last out).
def palindrome(head):
    # p2 is twice as fast, once reaches end, p1 at mid point, then the second half and the first half (since p2 back at head). Better solution is to go in reverse.
    def constant_space(head):
        p1 = p2 = head
        while p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            
        if p2.next:
            p2 = p2.next
            p1 = p1.next
            
        # Reversing linkedlist so that we can compare both sides of palindrome easier
        cur_node = reverse(p1)
        
        # Comparing both sides of palindrome by traversing through linkedlist
        original_head = head
        result = True
        # Maybe use better names...
        while cur_node.next != p1: # p1 midway point
            if cur_node.val != original_head.val:
                result = False
                break
            
            original_head = original_head.next
            cur_node = cur_node.next
            
        # mid_node = reverse(cur_node)
        
        return head, result
    # if odd linkedlist length
    
    # Using O(N) space
    def linear_space(head):
        stack = []
        p1 = p2 = head
        while p2.next.next:
            p1 = p1.next
            p2 = p2.next.next 
        # First get values from p1 (mid point to the end)
        # Then compare values from stack (using .pop()) and traversing through the first half of list
        mid_node = p1
        head_node = head 
        while p1.next:
            stack.append(p1.val)
            p1 = p1.next
        stack.append(p1.val)
        
        result = True
        while head_node != mid_node:
            if head_node.val != stack.pop().val:
                result = False
            head_node = head_node.next
            
        if head_node.val != stack.pop().val:
            result = False
            
        return head, result
        
    
    

# reverses linkedlist and returns new head node
def reverse(head):
    cur_node = head
    prev = None
    while cur_node.next:
        next = cur_node.next
        cur_node.next = prev
        prev = cur_node
        cur_node = next
    # This is example of special case, tail of linkedlist.
    cur_node.next = prev
    return cur_node  

# 2.7 Intersection: O(N^2) brute force way is to cmopare each element together. O(N) space is store values of first list as hashmap, traverse through second list, if node in hashmap[node.val]: return intersection
# Still need to test. I'm assuming you can use a range of data structures.
def intersection(head1, head2):
    def brute_force(head1, head2): # O(N^2)
        cur1 = head1
        cur2 = head2
        while cur1.next:
            while cur2.next:
                if cur1==cur2:
                    return True
                cur2 = cur2.next
            cur1 = cur1.next
    
    def using_hashmap(head1, head2):
        cur1 = head1
        hashmap = {}
        while cur1.next:
            if cur1.val in hashmap:
                hashmap[cur1.val].append(cur1)
            else:
                hashmap[cur1.val] = [cur1]
        hashmap[cur1.val] = cur1
            
        cur2 = head2
        # Shouldn't these if statements be constant? And if so, is this section of code j O(N)
        while cur2.next:
            if cur2.val in hashmap:
                if cur2 in hashmap[cur2.val]:
                    return intersection

# 2.8 Same thing as using_hashmap for 2.7. Prob some other 
def loop_detection(head):
    # Kinda want to assume that each .val is unique, esp looking at example... but I won't.  
    cur_node = head
    hashmap = {}
    while cur_node.next: 
        if cur_node.val in cur_node:
            if cur_node in hashmap[cur_node.val]:
                return cur_node
            hashmap[cur_node.val].append(cur_node)
        else:
            hashmap[cur_node.val] = [cur_node]
    
        
    
                       

