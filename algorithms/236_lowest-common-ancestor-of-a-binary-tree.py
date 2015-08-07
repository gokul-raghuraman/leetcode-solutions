class TreeNode:
		def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None

def getInOrder(root):
	if root is None:
		return []
	left = getInOrder(root.left)
	this = [root.val]
	right = getInOrder(root.right)
	return left + this + right

class Solution:
	def lowestCommonAncestor(self, root, p, q):
		if root is None or root == p or root == q:
			return root
		left = self.lowestCommonAncestor(root.left, p, q)
		right = self.lowestCommonAncestor(root.right, p, q)
		if left and right:
			return root
		elif left:
			return left
		elif right:
			return right


if __name__ == "__main__":
	"""
				Testing on the tree given in the leetcode example:

				    _______3(A)______
			       /                 \
			   ___5(B)__          ___1(C)__
			  /         \        /         \
			 6(D)     _2(E)_    0(F)       8(G)
			         /      \
			        7(H)    4(I)

    """
	A = TreeNode(3)
	B = TreeNode(5)
	C = TreeNode(1)
	D = TreeNode(6)
	E = TreeNode(2)
	F = TreeNode(0)
	G = TreeNode(8)
	H = TreeNode(7)
	I = TreeNode(4)

	A.left = B
	A.right = C
	B.left = D
	B.right = E
	C.left = F
	C.right = G
	E.left = H
	E.right = I

	sol = Solution()

	print(sol.lowestCommonAncestor(A, D, I).val)



