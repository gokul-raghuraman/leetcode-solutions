class Solution:

	def lengthOfLongestSubstring(self, s):

		# Map of char vs index
		map = {}
		left = -1
		right = 0

		maxLength = 0
		while right < len(s):
			prevOccurrence = map.get(s[right])
			map[s[right]] = right
			if prevOccurrence is not None:
				left = max(left, prevOccurrence)
			maxLength = max(maxLength, right - left)
			right += 1
		return maxLength

if __name__ == "__main__":
	sol = Solution()

	a = "abcabcdbb"
	print(sol.lengthOfLongestSubstring(a))