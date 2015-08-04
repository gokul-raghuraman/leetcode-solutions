class Solution:
	def longestCommonPrefix(self, strs):
		longestPrefix = ''
		if strs is None:
			return longestPrefix
		if len(strs) == 0:
			return longestPrefix

		i = 0
		while(i < len(strs[0])):
			
			char = strs[0][i]

			for string in strs:
				if i >= len(string):
					return longestPrefix
				if not string[i] == char:
					return longestPrefix
			longestPrefix += char
			i += 1

		return longestPrefix
				



if __name__ == "__main__":
	sol = Solution()
	print(sol.longestCommonPrefix(['abc']))

