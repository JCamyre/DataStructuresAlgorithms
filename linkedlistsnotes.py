# 2.1 If you can use additional space/temp buffer, hashmap most efficient way to store values and check if said value in hashmap
# For the O(1) space solution, iterating through linkedlist and having a runner to check value of all other nodes pretty simple, but effective. Don't forget about runners, esp for linkedlists.
# U only need cur.next = cur.next.next to "remove" a node?
# Their solution is even more genius than I thought. I thought you would have to check all nodes for each iteration, but you just need to check future nodes. 
# This means you don't have to check if runner node same as current node. 

# Doing the prev = None, if not prev: prev = head seems inefficient, can I do it differnt. Also when do I have to account for one more case when doing while cur.next:. I have to run one more thning of logic after while loop done.

# Using two runners to get to middle of linkedlist.
# Using stack data type, specifically for reversing linkedlist

# Tips/techniques/patterns

# 