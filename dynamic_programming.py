# tripleStep
# Brute force solution. Time complexity O(3^n) Space O(1), where n is number of steps
def cWays(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    return cWays(n-1) + cWays(n-2) + cWays(n-3)

print(cWays(4))
# Memoization: Cache the values of cWays(). cWays(n-1) = 2, cWays(n-2) = 12, cWays(n-4) = 162: Once other cWays(n-4), they can just access the value from hashmap.
# Use memo for variable name? Them reusing function name is interesting.
def cWays(n):
    hashmap = {}
    def way(n, hashmap):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif n in hashmap:
            return hashmap[n]
        else:
            # When entering a value to a hashmap, if another way(n) call has the same val in the hashmap, we won't have to waste computational power
            hashmap[n] = way(n-1, hashmap) + way(n-2, hashmap) + way(n-3, hashmap) # If you have this n value, all of its possible pathways is way() + way() + way()
            return hashmap[n]
        
    return way(n, hashmap)
print(cWays(4))
# Robot in a grid
# Check if square is off limit, check if at max x or y already, move(x+1, y) if doesn't work move(x, y+1), 
def robotMove(grid: list[list]):
    # Starting move(0, 0)
    def move(x, y):
        if x == -1 and y == -1:
            x, y = 0, 0
            
        if x == len(grid[0])-1 and y == len(grid)-1:
            return 'Path completed!'
        elif x > len(grid[1]) and y > len(grid[0]):
            return move(x-1, y-1)
        elif x > len(grid[1]):
            return move(x, y+1)
        elif y > len(grid[0]):
            return move(x+1, y)

# 8.3: Magic Index. Iterative better option since just looping through arr.
def magicIndex(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return f'Found magic index at {i}!'
# How to make more efficient. O(n) time and O(1) space. Prob some property I'm missing out on. 
# If not all distinct values, then cache values and check to see if in hashmap, if so skip it.

# 8.4: Power set, sounds like top-down where you break it up into subproblems. Don't know techniques for finding subsets.
# Maybe Doing all but first element, all but second element... Then for each of those get rid of another element (like a tree thing), really unoptimized tho. O(2^N). Use cache?

# 8.5: Recursive Multiply. Check for which digital is lower and iterate the range(smallest num)
# Iteratively: for i in range(a): result += b. Recursive: add(n): return add(n+a) if n == 0

# 8.6: General rules: When popping, push to lowest tower, when you can pop, pop lowest to one tower, pop next to another, then pop lower to larger val
# If there is a val on second/third tower (higher than the discs on third tower), push to that one. If there is 
# Algo for putting a two stack on top of a third disc: Pop 3 -> push tower 1 -> Pop 3 -> push tower 2 -> pop 1 -> push tower 2 -> pop 1 -> push 3
# Always push lowest value to other tower that is occupied
# Keep popping and pushing until you can't, then pop and push on to the next tower, but it's important to always priotorize tower 3 (elif tower 3[0] > cur_disc: push 3). 
# Always check if you can move ring from first tower (if tower1[0] < tower3[0] elif tower1[0] < tower2[0] elif tower2[0] < tower1[0] elif tower3[0] < tower1[0])
def hanoi(N):
    stacks = list(range(1, N+1)), [], []
    return hanoi(N, stacks[0], stacks[1], stacks[2])        

def hanoi(N, tower1, tower2, tower3):
    if len(tower3) == N:
        return 'Done!'
    elif tower1[0] < tower3[0]:
        tower3.push(tower1.pop())
    elif tower1[0] < tower2[0]:
        tower2.push(tower1.pop())
    elif tower2[0] < tower1[0]:
        tower1.push(tower2.pop())
    elif tower3[0] < tower1[0]:
        tower1.push(tower3.pop())
    return hanoi(N, tower1, tower2, tower3)
    
# 8.7 What if duplicate letters in given string? Use the tries???? It is the best for words. 
# Or could do loop through string starting with each letter, then for that function call pass in list of letters besides the one you are using, and repeat (the time complexity so baddd). Memoization??
# O(N^N) time complexity bruhh cause N different permutations per character and N characters total. I feel iterative better than recursion here

def permutations_wo_dups(string):
    return 

def permutations_wo_dups(cur_string, total_string):
    
