class Solution:
	def isPowerOfTwo(self, n):
		if n <= 0:
			return False
		while(n > 1):
			if n % 2 == 1:
				return False
			n = n / 2

		return True

if __name__ == "__main__":
	sol = Solution()
	print sol.isPowerOfTwo(32)