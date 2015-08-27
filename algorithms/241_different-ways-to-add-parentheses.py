class Solution:
	def diffWaysToCompute(self, input):
		if input.isdigit():
			return [int(input)]
		results = []
		for i in range(len(input)):
			if input[i] in "+-*":
				res1 = self.diffWaysToCompute(input[:i])
				res2 = self.diffWaysToCompute(input[i+1:])
				for res_i in res1:
					for res_j in res2:
						result = self.compute(res_i, res_j, input[i])
						results.append(result)
		return results

	def compute(self, res1, res2, operator):
		if operator == '+':
			return res1+res2
		elif operator == '-':
			return res1-res2
		else:
			return res1*res2

if __name__ == "__main__":
	sol = Solution()
	print(sol.diffWaysToCompute("2*3-4*5"))