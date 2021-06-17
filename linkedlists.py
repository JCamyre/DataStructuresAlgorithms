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