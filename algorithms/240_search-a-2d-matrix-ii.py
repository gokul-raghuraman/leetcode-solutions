class Solution:
	def searchMatrix(self, matrix, target):
		
		row = 0
		col = len(matrix[0]) - 1

		while row < len(matrix) and col >= 0:
			if matrix[row][col] == target:
				return True
			if matrix[row][col] > target:
				col -= 1
			elif matrix[row][col] < target:
				row += 1
			print("Traversing : (" + str(row) + ", " + str(col) + ")")
		return False


if __name__ == "__main__":
	matrix = [
		[1,   4,  7, 11, 15],
		[2,   5,  8, 12, 19],
		[3,   6,  9, 16, 22],
		[10, 13, 14, 17, 24],
		[18, 21, 23, 26, 30],
		[19, 24, 25, 28, 32],
		[21, 25, 26, 29, 34],
		[21, 27, 28, 31, 37],
	]
	sol = Solution()
	print(sol.searchMatrix(matrix, 31))



