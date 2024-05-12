class myStack:
  #Please read sample.java file before starting.
  #Kindly include Time and Space complexity at top of each file
  # Time Complexity: O(1)
  # Space Complexity: O(n)
     def __init__(self):
         self.stack = []
     def isEmpty(self):
         return False if self.stack else True
         pass
     def push(self, item):
         self.stack.append(item)
         pass
     def pop(self):
         return self.stack.pop()
         pass
     def peek(self):
         return self.stack[-1]
     def size(self):
         return len(self.stack)
     def show(self):
         return (self.stack)

s = myStack()
s.push('1')
s.push('2')
print(s.peek())
print(s.isEmpty())
print(s.pop())
print(s.show())