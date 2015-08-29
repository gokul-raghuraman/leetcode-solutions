from collections import deque

class Solution:
	def maxSlidingWindow(self, nums, k):

		# Edge case, if empty input, return empty output
		if nums == []:
			return []

		n = len(nums)

		# Create an empty result array of size n-k+1
		result = [0 for i in range(n-k+1)]

		# Initialize a double-ended queue
		dq = deque()

		# Go through the first k values and store their indices
		# in decreasing order of their values. Keep popping until
		# Right-most element in deque is greater than (or equal to)
		# nums[i]. Index of max-valued element will be on the left.
		for i in range(k):
			while dq and nums[i] > nums[dq[-1]]:
				dq.pop()
			dq.append(i)

		# Now to get the result array, iterate n-k times
		for i in range(n-k):
			# result[i] will be the max value, which is left-most element 
			# of the deque 
			result[i] = nums[dq[0]]

			# Now, pop out all elements which are going to be at index i
			# or less, preparing for the next iteration.
			while dq and dq[0] <= i:
				dq.popleft()

			# Now, in preparing for the next new number, pop out all elements
			# that are less than nums[i+k]. Why i+k? Remember we have already 
			# done this for i+k-1 elements above.
			while dq and nums[i+k] > nums[dq[-1]]:
				dq.pop()

			# Now append the next element to deque
			dq.append(i+k)

		# Last iteration.
		result[-1] = nums[dq[0]]
		return result

if __name__ == "__main__":
	sol = Solution()
	nums = [1, 3, -1, -3, 5, 3, 6, 7]
	print(sol.maxSlidingWindow(nums, 3))