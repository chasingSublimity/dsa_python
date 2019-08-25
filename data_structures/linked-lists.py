class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node

  def __str__(self):
    return str(self.value)


class LinkedList:
  def __init__(self, head_node_value):
    self.head_node = Node(head_node_value)

  def __str__(self):
    return str([n.value for n in self.lazy_traversal()])

  def add_to_beginning(self, value):
    new_head = Node(value)
    new_head.next_node, self.head_node = self.head_node, new_head

  def remove_node(self, value_to_remove):
    if self.head_node.value == value_to_remove:
      self.head_node = self.head_node.next_node
    else:
      current_node = self.head_node
      while current_node:
        if current_node.next_node.value == value_to_remove:
          current_node.next_node = current_node.next_node.next_node
          break
        else:
          current_node = current_node.next_node

  def contains_value(self, value_to_find):
    return value_to_find in self.lazy_traversal()

  def lazy_traversal(self, node=None):
    current_node = node if node is not None else self.head_node
    
    while current_node:
      yield current_node
      current_node = current_node.next_node

ll = LinkedList(24)
ll.add_to_beginning(46)
ll.add_to_beginning(84)
print(ll)
ll.remove_node(46)
print(ll)

print(ll.contains_value(24))
print(ll.contains_value(46))
