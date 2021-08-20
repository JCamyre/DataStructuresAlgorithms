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
    while cur.next:
        yield cur
        cur = cur.next
    yield cur

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
    # O(n) space solution, O(n) time tho!! Can use a hashmap too. Better for checking if val in keys. 
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
        print('NEW LOOP')
        # Testing starting at head
        cur = the_head
        prev = None
        unsorted = False
        
        while cur.next:
            print('Cur val: ', cur.val)
            next_node = cur.next

            if cur.val > cur.next.val:
                print(prev, cur.val, cur.next.val, next_node.next.val) # We want to cur.next.next = cur, cur.next = cur.next.next 2 -> 4 -> 3
                if prev:
                    prev.next = next_node
                next_next_node = next_node.next
                next_node.next = cur
                cur.next = next_next_node
                
                print() # We want to cur.next.next = cur, cur.next = cur.next.next 2 -> 4 -> 3

                # cur.next = cur.next.next
                # next_node.next = cur
                # next_node = cur.next
                unsorted = True
                if not prev:
                    the_head = cur.next
            
            for node in iterate_linked_list(cur):
                print(node, end=' -> ')
            print('')
                
            prev = cur                    
            cur = cur.next

        # if cur.val > cur.next.val:
        #     next_node = cur.next
        #     prev.next = next_node
        #     cur.next = cur.next.next
        #     next_node.next = cur        
        #     if not prev.val:
        #         the_head = cur.next
        
        # Their solution is iterates through the linked list, and a "runner" which for each iteration checks all other elements in the linked list.
        # Their solution is not good, because what if duplicates 
                
        if not unsorted:
            break
        
    return the_head
            
    

linked_list = create_linked_list([4, 2, 3, 3, 2])

for node in iterate_linked_list(remove_dups(linked_list)):
    print(node)

# 2.2
# Brute force O(1) space: Sorta like 2.1 using a "runner" sorta. For the cur node, run a for loop for the range of kth to element loop, if statement for if not cur.next:
# Basically O(N^2). 
# Can't go to the end of the list and work way back because we don't keep track of .prev (that double linked list)
# Anyway to improve runtime with some space? Add all nodes to an array, then take the kth to last element slice/index. O(n) TIME, O(n) space
# Can try splitting up into multiple functions
def return_kth_to_last(k, head): 
    # O(1) space: 
    if k <= 0:
        return head
    
    cur = head
    while cur.next:
        for _ in range(k):
            # One thing to watch out: If len(linkedlist) > k, then the first node where cur.next == None. If shorter than linkedlist, problem. 
            if not cur.next:
                return None
            cur = cur.next 
        # If the next node after k nodes is None, we r at the end of the linkedilst
        if not cur.next: # End of the linked list!!
            return cur
        cur = cur.next
    
    # If there is only one node left, k would have to be 0, so don't need to account for this case, if we are assuming k>0
    
    # return head

    # O(n) space and time
    def return_all_nodes(head):
        cur = head 
        while cur.next:
            yield cur
            cur = cur.next
            
            
    nodes = return_all_nodes(head)
    if len(nodes) > k:
        return nodes[-k]
    return None

    # Could use recursion: Remember that recursive solutions are often cleaner but less optimal.
    # They use recursion + a counter to start counting once reach end of linkedlist. The code a little wack.
    # Not really vibing with the recursion solutions. RECURSIVE SOLUTIONS TAKE O(N) SPACE DUE TO THE RECURSIVE CALLS.
    # Maybe review recursive solutions, I just prefer iterative solutions
    
    # Iterative solutions: A proper pointer solution, basically less scuffed version of my first idea. 
    # Have p1 at head of list, and p2 at k elements away. Once p2 at end of list, p1 is the kth element from the end.
    # Make sure to check p2 not out of bounds (linkedlist too small), use for loop like I did to put it k elements away.
    
# 2.3
# Any possible way to access nodes before it? 
# We don't have to access head node, all we need to do is connect previous node to the node after the one we are deleting. 
# Their solution is a very interesting way of "deleting" a node. We will copy the val from the next node to the given node, and delete the next node.
# This means we don't have to do anything with relinking the nodes. So by "delete", we don't delete the exact node object, just copy the value and delete the node that we can delete.
# Delete = replace value and delete the next node. 

# Visualization: A -> B -> C -> D. A -> C -> C -> D. Delete original C node. A -> C -> D
# Just know: When deleting, don't have to necessarily delete exact object, can "delete" by copying value and deleting the original node with the copied value.

# "Note that this problem cannot be solved if the node to be deleted is the last node in the linked list. That's
# okay- your interviewer wants you to point that out, and to discuss how to handle this case. You could, for
# example, consider marking the node as dummy."
# But the problem stated not head or tail node.

def delete_middle_node(node):
    if not node or not node.next:
        return False
    
    next_node = node.next
    node.val = next_node.val
    node.next = next_node.next
    return True
    
   # When thinking of solutions, consider ones that seem jank or don't completly satsify problem.

# 2.4 The two sides don't have to be sorted
# Add to either the head or the tail, depending on its val
# Instead of tail, iterate through linkedlist until value greater than or equal to value x
# def partition_linked_list(value, head):
#     cur = head
#     prev = None
#     while cur.next:
#         next_cur = cur.next
#         if cur.val >= value: # put value to right side
#             pointer = cur
#             next_node_to_iterate = cur.next
#             while pointer.next:
#                 if pointer.val > value:
#                     prev = 
#                     next_node = pointer.next # temp store value
#                     pointer.next = cur
#                     cur.next = next_node
#                     # HAVE TO GO BACK TO 1, STORE THE VALUE previous to cur?
#                     cur = next_node_to_iterate
#                     break

#                 pointer = pointer.next
#         else: # left side
#             next_node = cur.next # 4
#             cur.next = head # 1
#             if prev: # None
#                 prev.next = next_node # 1 -> 3
#             else:
                
        
#         prev = prev.next
#         cur = next_cur

# Their solution is so much easier: Iterate through linkedlist and append to two separate linkedlists. Then merge at the end. 
# Note: Array shifts are very expensive since we have to update the index for every single element after the element we inserted
# If we don't care about making the elements of the list "stable" (which there's no obligation to, since the
# interviewer hasn't specified that), then we can instead rearrange the elements by growing the list at the
# head and tail.
# Update either the head or tail (like what I said sort of)
# I should have done better with this one
def partition(head, x):
    cur = head.next
    greater = head
    lesser = head
    
    while cur.next:
        next_node = cur.next
        if cur.val > x:
            # Honestly this solution isn't intuitive to me, I need to study this.
            cur.next = greater # could also do cur.next = greater, but would have to save next_node = cur.next
            greater = cur
        else:
            cur.next = lesser
            lesser = cur
        cur = next_node
    
    greater.next = None
        
    return lesser 
# Using multiple linkedlists for a solution is interesting... Using multiple of things I should apply to more problems

# 2.5 I'll admit, I remember this solution from Leetcode. Such a meta solution, using the principles from first grade arithmetics.
# Don't assume same length for both lists. Return the linkedlist not reversed right?
def sum_lists(head1, head2):
    cur1 = head1
    cur2 = head2
    the_sum = 
    while cur1.next and cur2.next:
        
        value = cur1.val + cur2.val # This can't be value, cause we aren't putting 12 for a node
        if the_sum:
            node = LinkedListNode(value)
            node.next = the_sum
            the_sum = node
        if value > 
        carry = value % 10
# These mfs using recursion bruh. I iteration only :sunglasses:. Need more recursion practice.

# 2.6 Using O(n) space: Use hashmap and iterate through linkedlist, adding to hashmap. If anymore than one thing have only one character, not palindrome.
# Using recursion: check if .next, is_palindrome(p.next, values), have a hashmap passed through
# Using no space, save head, and reverse the list. Then compare the two versions. Anything better than O(1) space and O(n^2) time?
# A small optimization for the O(1) space: Since palindrome is same forward and back, only have to check first half of regular linkedlist and half of reversed linkedlist

# Another solution using space, but only half as much. Use a stack to reverse the first half of the linkedlist (we have to be careful when dealing with odd length linkedlist)
# Use two runners (one twice as long) to get to the middle of the linkedlist. We then compare the nodes from the stack, to the second half of the linkedlist. If all equal, than palindrome.
# Need to get better at working with odd length or any edge case: if (fast != nUll) {slow = slow. next;}

# Recursion approach always yikes: 
# I like how they visualize the call stack
# Use length-2 to find the length of the linkedlist. 
# Compare node i to node n-i (since palindromes are same forward and back)
# Very interesting use of call stacks and "rewinding them". Basically "on the way down" we are making a call stack from the first node to one node before the middle node, 
# And "on the way back up" we are comparing the node after the middle to the node before the middle, then we compare two nodes after middle to two nodes before. We are returning the second half of nodes "on the way back up".
# It is very smart, I hope it makes sense. call 1 -> call 2 -> call 3 -> call 4 (hit middle) > call 3 compared to first node in second half -> call 2 compared to second node in second half -> call 1 compared to last node in second half
# Have to do the length - 2 to find halfway point. Very cool

# 2.7 intersection:
# Very easy O(n^2) time and O(1) space for each node in List A to be compared to every node in List B
# Finding middle node doesn't matter, reversing list doesn't necessarily help
# Only way to make more efficient is to not have to compare each node O(n^2)
# Using space: Iterate through List A and put in all nodes in an array. Then compare to List B, O(n) time and space.
# Only have to find one intersecting node
# If two lists are intersecting, every node after the first intersecting node are the same. This means they will always have the same tail node.
# This why working through examples while rereading the prompt is so important.
# Count the length of each list and get the tail nodes. If the tail nodes !=, then return because there is no intersection.
# If there is a difference in the lists, the longer list will have useless nodes, so we will skip them by having a pointer that is abs(length1-length2) ahead of pointer2
# Once they are the same object, return.
# There's always some optimization trick, just got to work through the problem. Finding the length and tail node seems a little inefficient, but works clean.

# 2.8 Brute force use hashmap to store nodes. Check if node in it.
# Check if current node in hashmap
# The two runner thing is broken: if in a circular list, they will always eventually meet. They can not skip each other: if slow is i and fast is i + 1, then the previous step was i - 1 and (i + 1) - 2 = i - 1. BOOM
# So if the list is circular, with the slow and fast runner, they will eventually collide. 
# So how long until they collide? If the size of the non-looped part is size K, 2(K) - 2
# Some math behind it, sorta understand it. Because of the difference of nodes traveled, when they collide, the next time they meet when slowpointer is reset, that is when loop should be.
# Slow + fast pointer, when they collide, keep fast pointer where it is and reset slow pointer. Then move them both at a rate of one step. When they collide, this is where loop is.

