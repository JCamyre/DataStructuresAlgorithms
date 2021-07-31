from linkedlists import SingleLinkedNode

class StackLinkedList:
    def __init__(self, arr):
        self.head = SingleLinkedNode(arr[0])
        for val in arr[1:]:
            self.head.next = SingleLinkedNode(val)
            self.head = self.head.next
    
    def pop(self):
        pass
    
    def push(self, item):
        pass
    
    def peek(self):
        pass
    
    def isEmpty(self):
        pass
    
    def __len__(self):
        pass
    
    def __bool__(self):
        pass
            
            

class Stack:
    def __init__(self, arr): # user can initialize Stack with array of elements
        self.stack = arr
    
    def pop(self):
        popped_element = self.stack[-1]
        self.stack = self.stack[:-1]
        return popped_element

    def push(self, item):
        self.stack.append(item)
        
    def peek(self):
        if self.stack:
            return self.stack[-1]
        return None
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        return f'Length: {len(self.stack)}, top item: {self.peek()}'
    
    def __len__(self):
        return len(self.stack)
    
    def __bool__(self):
        return 

stack = Stack([1, 2, 3])
print(stack)
print(stack.push(4))
print(stack)
# Can be implemented using linkedlists

class Queue:
    def __init__(self, queue): # user can initialize Queue with array of elements
        self.queue = queue
    
    def pop(self):
        popped_element = self.queue[0]
        self.queue = self.queue[1:]
        return popped_element

    def push(self, item):
        self.queue.append(item)
        
    def peek(self):
        return self.queue[-1]
    
    def isEmpty(self):
        return len(self.queue) == 0