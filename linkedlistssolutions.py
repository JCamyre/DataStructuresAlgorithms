# 1.1
# Questions: Are they int for the values (could be used for solution)
# Brute force: Account for no linkedlist or only one node. If we can use space, obv just append values and check if cur.val in vals. 
# Manually sort? Check vals of cur node with next node. Save the head initial head val. Keep on sorting until loop doesn't break. Have an if statement for each loop that checks if cur.val > next.val. Break if not true.

# Second while loop: compare adjacent values. 
# This prob an O(n log n), j cause that what most sorting algorithms are. Better than O(n^2) for sure.
# Reverse linked list, and compare the two as you iterate through (THIS WON'T WORK)

# Very easy to remove nodes

class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
        
def iterate_linked_list(head):
    cur = head
    nodes = []
    while cur.next:
        nodes.append(cur)
        cur = cur.next
    nodes.append(cur)
    return nodes

def create_linked_list(vals):
    if len(vals) <= 0:
        return 0
    
    head = LinkedListNode(vals[0])
    cur = head
    for i in vals[1:]:
        cur.next = LinkedListNode(i)
        cur = cur.next
    
    return head

def remove_dups(head):
    # O(n) space solution, O(n) time tho!!
    arr = []
    the_head = head 
    cur = head
    # Can either keep track of prev or while cur.next.next and check if cur.next.val in arr:
    prev = None
    while cur.next:
        if cur.val in arr:
            prev.next = cur.next
        else:
            arr.append(cur.val)
        prev = cur
        cur = cur.next
    # Is there more efficiency way to handle last case?
    if cur.val in arr:
        prev.next = cur.next
    
    # return the_head

    # O(1) space solution, O(n log n) or worse
    # tracks for this iteration if an unsorted element
    # have to update head node
    # This is called bubble sort
    the_head = head
    while True:
        cur = head
        prev = None
        unsorted = False
        while cur.next:
            if cur.val > cur.next.val:
                next_node = cur.next
                if prev:
                    prev.next = next_node
                cur.next = cur.next.next
                next_node.next = cur
                unsorted = True
                if not prev:
                    the_head = cur.next
                    
            prev = cur                    
            cur = cur.next

        # if cur.val > cur.next.val:
        #     next_node = cur.next
        #     prev.next = next_node
        #     cur.next = cur.next.next
        #     next_node.next = cur        
        #     if not prev.val:
        #         the_head = cur.next
                
        if not unsorted:
            break
        
    return the_head
            
    

linked_list = create_linked_list([4, 2, 3, 3, 4])

for node in iterate_linked_list(remove_dups(linked_list)):
    print(node)
