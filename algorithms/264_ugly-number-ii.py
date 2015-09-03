"""
Attempted approach
Think of ugly numbers as being either multiples of 2, 3, or 5
Let's maintain 


n = 11

l1 = [1]
i = 0
j = 0
k = 0

minNum = min(l1[i]*2, l1[j]*3, l1[k]*5) = min(2, 3, 5) = 2
l1 = [1, 2]
i = 1
j = 0
k = 0

minNum = min(l1[i]*2, l1[j]*3, l1[k]*5) = min(4, 3, 5) = 3
l1 = [1, 2, 3]
i = 1
j = 1
k = 0

minNum = min(l1[i]*2, l1[j]*3, l1[k]*5) = min(4, 6, 5) = 4
l1 = [1, 2, 3, 4]
i = 2
j = 1
k = 0

minNum = min(l1[i]*2, l1[j]*3, l1[k]*5) = min(6, 6, 5) = 5
l1 = [1, 2, 3, 4, 5]
i = 2
j = 1
k = 1

minNum = min(l1[i]*2, l1[j]*3, l1[k]*5) = min(6, 6, 10) = 6
l1 = [1, 2, 3, 4, 5, 6]
i = 3
j = 2
k = 1

minNum = min(l1[i]*2, l1[j]*3, l1[k]*5) = min(8, 9, 10) = 8
l1 = [1, 2, 3, 4, 5, 6, 8]
i = 4
j = 2
k = 1

minNum = min(l1[i]*2, l1[j]*3, l1[k]*5) = min(10, 9, 10) = 9
l1 = [1, 2, 3, 4, 5, 6, 8, 9]
i = 4
j = 3
k = 1

minNum = min(l1[i]*2, l1[j]*3, l1[k]*5) = min(10, 12, 10) = 10
l1 = [1, 2, 3, 4, 5, 6, 8, 9, 10]
i = 5
j = 3
k = 2

minNum = min(l1[i]*2, l1[j]*3, l1[k]*5) = min(12, 12, 15) = 12
l1 = [1, 2, 3, 4, 5, 6, 8, 9, 10]
i = 6
j = 4
k = 2

minNum = min(l1[i]*2, l1[j]*3, l1[k]*5) = min(16, 15, 15) = 15
l1 = [1, 2, 3, 4, 5, 6, 8, 9, 10]
i = 6
j = 5
k = 3
"""

class Solution:
	def nthUglyNumber(self, n):
		if n == 1:
			return 1
		
		i = 0
		j = 0
		k = 0
		l1 = [1]

		counter = 0
		while counter < n-1:
			minNum = min(l1[i]*2, l1[j]*3, l1[k]*5)
			if minNum == l1[i] * 2:
				i += 1
			if minNum == l1[j] * 3:
				j += 1
			if minNum == l1[k] * 5:
				k += 1
			l1.append(minNum)
			counter += 1

		return minNum

if __name__ == "__main__":
	num = 3
	sol = Solution()
	print(sol.nthUglyNumber(num))