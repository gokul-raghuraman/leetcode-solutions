class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# For in-order traversal
def inOrder(node):

	if node is None:
		return
	inOrder(node.left)
	print(node.val)
	inOrder(node.right)

def getSums(node, pathSum):
	sumLeft = 0
	sumRight = 0
	if node is None:
		return pathSum
	if node.left is None and node.right is None:
		return pathSum * 10 + node.val
	if node.left is not None:
		sumLeft = getSums(node.left, pathSum * 10 + node.val)
	if node.right is not None:
		sumRight = getSums(node.right, pathSum * 10 + node.val)
	return (sumLeft + sumRight)

if __name__ == "__main__":
	A = TreeNode(1)
	B = TreeNode(3)
	C = TreeNode(2)
	D = TreeNode(1)
	E = TreeNode(4)
	F = TreeNode(2)
	G = TreeNode(7)
	A.left = B
	A.right = C
	B.left = D
	B.right = E
	C.left = F
	C.right = G

	print(getSums(A, 0))
