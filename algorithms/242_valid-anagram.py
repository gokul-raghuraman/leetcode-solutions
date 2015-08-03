class Solution:
	def isAnagram(self, s, t):
		dict = {}
		for char in s:
			if dict.get(char):
				dict[char] += 1
			else:
				dict[char] = 1

		for char in t:
			if dict.get(char):
				dict[char] -= 1
			else:
				dict[char] = 1

		for key in dict:
			if dict[key] != 0:
				return False

		return True

if __name__ == "__main__":
	sol = Solution()
	s = "a"
	t = "ab"
	print(sol.isAnagram(s, t))
