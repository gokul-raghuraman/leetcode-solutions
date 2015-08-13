class Solution:
	def reverse(self, x):
		negative = x < 0
		if negative:
			x = -x
		newNum = 0
		while x > 0:
			digit = x % 10
			x = x / 10
			newNum = newNum * 10 + digit
		if newNum > 0x7fffffff:
			return 0
		if negative:
			newNum *= -1
		return newNum



if __name__ == "__main__":
	sol = Solution()
	print(sol.reverse(-123))