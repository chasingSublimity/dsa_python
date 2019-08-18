class Node():
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node


class LinkedList():
  def __init__(self, head_node_value):
    self.head_node = Node(head_node_value)

  def add_to_beginning(self, value):
    new_head = Node(value)
    new_head.next_node = self.head_node
    self.head_node = new_head

  def stringify_list(self):
    string = ''
    current_node = self.head_node
    while current_node:
      string += f'{str(current_node.value)}\n'
      current_node = current_node.next_node
    return string

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
    current_node = self.head_node
    while current_node:
      if current_node.value == value_to_find:
        return True
      else:
        current_node = current_node.next_node
    return False

ll = LinkedList(24)
ll.add_to_beginning(46)
ll.add_to_beginning(84)
print(ll.stringify_list())
ll.remove_node(46)
print(ll.stringify_list())

print(ll.contains_value(24))
print(ll.contains_value(46))
