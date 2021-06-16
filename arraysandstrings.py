class HashTable():  
    def __init__(self):
        self.arr = [None] * 20
    
    def append(self, key, val):
        hashed_key = hash(key)
        i = hashed_key % len(self.arr)
        # Could also use balanced binary tree. Should I store hashed_key or regular key?
        node = SingleLinkedNode(val={hashed_key: val})
        # might have issue with this line, since we Python array are dynamically changing in size, there won't be any spaces available, which means there will never be an empty element
        # could do self.arr = [None] * 20
        if self.arr[i]:
            cur_node = self.arr[i]
            while cur_node.next: # traversing
                cur_node = cur_node.next
            cur_node.next = node
        else:
            self.arr[i] = node
            
    def display(self):
        for i in range(len(self.arr)):
            if self.arr[i]:
                cur_node = self.arr[i]
                while cur_node.next:
                    print(cur_node.val)
                    cur_node = cur_node.next
                print(cur_node.val)
                
    def find(self, key):
        hashed_key = hash(key)
        i = hashed_key % len(self.arr)
        if self.arr[i]:
            cur_node = self.arr[i]
            while cur_node.next:
                if hashed_key in cur_node.val:
                    print(key, cur_node.val[hashed_key])
                cur_node = cur_node.next
            if hashed_key in cur_node.val:
                print(key, cur_node.val[hashed_key])
            
                               
# Kinda weird, but I think this is right: for the val, store {key: val}
class SingleLinkedNode():
    def __init__(self, val=None):
        self.val = val
        self.next = None
    
# different hash value every time
hashtable = HashTable()
def testing(dict):
    # for key, val in dict.items():
    for key, val in zip('abcdefghij', list(range(10))):
        hashtable.append(key, val)
    
    for key in 'abcdefjghij':
        hashtable.find(key)
        
    hashtable.display()
    

    
    
    
    
    
    
# 1.1: Most obvious would be to use hash table. How much more efficient is hash table than dictionary?
# Just loop through string, map each letter to hash map/dictionary. If letter already in hashmap, return False.
def is_unique(string):
    hash = {}
    for x in string:
        if x in hash: # assuming x in hash is constant time, maybe linear time
            return False
        else:
            hash[x] = x
    return True

# Another way is to sort list, then sliding window to see if next character the same. O(NlogN*N)

# Brute force is loop through every letter, then another for loop inside looping besides n, n++, O(N^2)
def is_unique_bruteforce(string):
    n = 0
    for i in range(len(string)):
        for j in range(len(string)):
            if string[i] == string[j] and i != j:
                return False
        n += 1
    return True

# Best conceivable runtime (BCR) is O(N), since you have to loop through all elements atleast once.

# 1.2 another hashmap, very obv. if hashmap[i]: hashmap[i] += 1; else: hashmap[i] = 1

# 1.3. For Python, very obv (split(), replace()). All are O(N)
def urlify(string):
    print('%20'.join(string.split()))
    print(string.replace(' ', '%20'))
    arr = []
    for i in range(len(string)):
        if string[i] == ' ':
            arr[i] = '%20'
        else:
            arr[i] = string[i]
    print(''.join(arr))
    
# 1.4 string[:n] == string[n:]. Only problem is if odd N length. Also have to consider white space. Could do hashtable and check to see how many of each character. There has to be a certain/matching number of even and odd frequency of characters. 
# I can't think of the pattern rn...

# 1.5 Brute force: Loop through both strings, if either not equal, a+=1. Have first if statement(a < 1) {return False}

# 1.6 Loop through, Use hashtable. Brute force way of checking which is longer, make new string and compare which ever is longer. Better way: compare len(dict)*2 == original string.

# 1.7 2d list, if at end of list, move down vertically, YO THIS ONE IS SUSSSY. If 

# 1.8 Looping through the 2d list, if(x==0){arr[i]=[0]*length of array}, then loop through all arrays and set arr[i]=0 vertically.

# 1.9 I'll think about this one