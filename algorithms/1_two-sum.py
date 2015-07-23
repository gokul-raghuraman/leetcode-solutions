class Solution:
	# @param {integer[]} nums
	# @param {integer} target
	# @return {integer[]}
	def twoSum(self, nums, target):
		twoSumMap = {}
		for i, num in enumerate(nums, start=1):
			if target-num in twoSumMap:
				return [twoSumMap[target-num], i]
			twoSumMap[num] = i

if __name__ == "__main__":
	nums = [2, 7, 11, 15]
	target = 9
	sol = Solution()
	print(sol.twoSum(nums, target))
