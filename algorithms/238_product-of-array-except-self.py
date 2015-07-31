class Solution:
	def productExceptSelf(self, nums):
		productToIndex = [1]
		productFromIndex = [1]
		productExceptSelf = []
		for i in range(1, len(nums)):
			productToIndex.append(productToIndex[i-1] * nums[i-1])
		for i in range(1, len(nums)):
			productFromIndex.append(productFromIndex[i-1] * nums[len(nums)-i])
		productFromIndex.reverse()
		for i in range(len(nums)):
			productExceptSelf.append(productToIndex[i] * productFromIndex[i])
		return productExceptSelf


if __name__ == "__main__":
	a = [2, 3, 1, 7, 8]

	sol = Solution()
	sol.productExceptSelf(a);