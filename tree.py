# Hierarchical Data Structure


class TreeNode:
	def __init__(self, value):
		self.value = value
		self.children = []


	def add_child(self, child_node):
		self.children.append(child_node)


# Examples
root = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')

root.add_child(b)
root.add_child(c)