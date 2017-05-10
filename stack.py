class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return self.items == []
  def push(self,item):
    self.items.append(item)
  def pop(self):
    return self.items.pop()
  def peek(self):
    return self.items[len(self.items) - 1]
  def size(self):
    return len(self.items)


s=Stack()

print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
print (s.items)

def rev_string(string):
    rev_str = Stack()
    # push all characters into stack.
    for c in string:
        rev_str.push(c)

    # Build a new reverse string and return it
    rev_str1 = ""
    while rev_str.size():
        rev_str1 += rev_str.pop()
    return rev_str1

print (rev_string("peace"))
