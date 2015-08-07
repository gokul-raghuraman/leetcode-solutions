class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:

	def isPalindrome(self, head):
		if head is None:
			return True

		length = self.getLength(head)
		pointer1 = head
		pointer2 = self.reverseSecondHalf(head, length)
		while pointer2 is not None:
			if not pointer1.val == pointer2.val:
				self.reverseSecondHalf(head, length)
				return False
			pointer1 = pointer1.next
			pointer2 = pointer2.next
		self.reverseSecondHalf(head, length)
		return True


	def getLength(self, head):
		if head is None:
			return 0
		cur = head
		count = 0
		while cur is not None:
			count += 1
			cur = cur.next
		return count

	def printList(self, head):
		cur = head
		printList = []
		while cur is not None:
			printList.append(str(cur.val))
			cur = cur.next
		print("->".join(printList))


	def reverseSecondHalf(self, head, length=None):
		if length is None:
			length = self.getLength(head)
		start = (length + 3) / 2
		startNode = head
		i = 1
		joinNode = None
		while(i < start):
			if i == start - 1:
				joinNode = startNode
			startNode = startNode.next
			i += 1

		prevNode = None
		curNode = startNode
		
		#Reverse second half as a separate list (it has no idea of the first half)
		while curNode is not None:
			nextNode = curNode.next
			curNode.next = prevNode
			prevNode = curNode
			curNode = nextNode

		#Now join the second half to the end of the first.
		joinNode.next = prevNode

		#Return the head of the second half
		return prevNode

if __name__ == "__main__":
	a = ListNode(1)
	b = ListNode(2)
	c = ListNode(3)
	d = ListNode(3)
	e = ListNode(2)
	f = ListNode(1)
	a.next = b
	b.next = c
	c.next = d
	d.next = e
	e.next = f

	sol = Solution()
	
	print(sol.isPalindrome(a))

