class SingleLinkedNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def __str__(self):
        return str(self.val)
        
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

head = SingleLinkedNode(5)
cur_node = head
for i in range(4, 0, -1):
    cur_node.next = SingleLinkedNode(i)
    cur_node = cur_node.next

tail = reverse(head)
print(tail, tail.next)
while tail.next:
    print(tail)
    tail = tail.next
print(tail)