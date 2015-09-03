class Solution:
	def isUgly(self, num):
		reducedNum = num
		while reducedNum >= 2:
			if reducedNum % 2 == 0:
				reducedNum /= 2
			else:
				break
		while reducedNum >= 3:
			if reducedNum % 3 == 0:
				reducedNum /= 3
			else:
				break
		while reducedNum >= 5:
			if reducedNum % 5 == 0:
				reducedNum /= 5
			else:
				break

		if reducedNum == 1:
			return True

		return False


if __name__ == "__main__":
	sol = Solution()

	num = 11
	print(sol.isUgly(num))