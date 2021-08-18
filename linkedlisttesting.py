class LinkedListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)

def create_linked_list(vals):
    if len(vals) <= 0:
        return 0
    
    head = LinkedListNode(vals[0])
    cur = head
    for i in vals[1:]:
        cur.next = LinkedListNode(i)
        cur = cur.next
    
    return head

def iterate_linked_list(head):
    cur = head
    while cur.next:
        yield cur
        cur = cur.next
    yield cur
    
# 4 -> 2 -> 3
linked_list = create_linked_list([4, 2, 3])
# for node in iterate_linked_list(linked_list):
#     print(node)

the_head = linked_list
cur = the_head
prev = None
while cur.next:
    if cur.val > cur.next.val:
        next_node = cur.next
        print(next_node)
        cur.next = cur.next.next
        next_node.next = cur
        if prev:
            prev.next = cur
        if not prev:
            the_head = next_node
    
    prev = cur
    cur = cur.next
    
print(the_head)