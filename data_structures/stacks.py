class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def __str__(self):
    return str(self.value)

class Stack:
  def __init(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit

  def push(self, value):
    if self.has_space():
      item = Node(value)
      item.next_node = self.top_item
      self.top_item = item
      self.size +=1
    else:
      print('No space!')

  def pop(self):
    if not self.is_empty():
      item = self.top_item
      self.top_item = self.top_item.next_node
      self.size -= 1
      return item

  def peak(self):
      return self.top_item.value if not self.is_empty() else None

  def has_space(self):
    return self.size < self.limit
  
  def is_empty(self):
    return self.size == 0