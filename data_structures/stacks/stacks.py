from node import Node

class Stack:
  def __init__(self, limit=1000):
    self.head = None
    self.size = 0
    self.limit = limit

  def __len__(self):
    return self.size
  
  def __str__(self):
    array = []
    current_node = self.head
    while current_node.next_node:
      array.append(current_node)
      current_node = current_node.next_node
    return str(array)

  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.next_node = self.head
      self.head = item
      self.size +=1
    else:
      raise IndexError()

  def pop(self):
    if not self.is_empty():
      item = self.head
      self.head = self.head.next_node
      self.size -= 1
      return item.value
    
  def peak(self):
      return self.head.value if not self.is_empty() else None

  def has_space(self):
    return self.size < self.limit
  
  def is_empty(self):
    return self.size == 0

