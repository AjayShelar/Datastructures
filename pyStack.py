
# coding: utf-8

# In[4]:

from pythonds.basic.stack import Stack

class Stack:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)

s = Stack()

print(s.isEmpty())
print(s.size())
s.push(10)
s.push('AJAY')
s.push("hi this is Sanjay")
print(s.peek())
print(s.size())
s.pop()
s.pop()
print(s.peek())
print(s.size())
print(s.isEmpty())

