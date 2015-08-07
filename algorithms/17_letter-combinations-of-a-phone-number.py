class Solution:

	lookup = {
			"2" : ["a", "b", "c"],
			"3" : ["d", "e", "f"],
			"4" : ["g", "h", "i"],
			"5" : ["j", "k", "l"],
			"6" : ["m", "n", "o"],
			"7" : ["p", "q", "r", "s"],
			"8" : ["t", "u", "v"],
			"9" : ["w", "x", "y", "z"]
		}

	def letterCombinations(self, digits):
		if len(digits) == 0:
			return []
		if len(digits) == 1:
			return self.lookup.get(digits[0])

		allCombos = []
		combosSoFar = self.letterCombinations(digits[:-1])
		letters = self.lookup.get(digits[-1])

		for i in range(len(letters)):
			for j in range(len(combosSoFar)):
				allCombos.append(combosSoFar[j] + letters[i])
		return allCombos


if __name__ == "__main__":
	sol = Solution();
	print(sol.letterCombinations("46585"))