class Solution:

	def toBinary(self, num):
		binaryStr = ''
		while num > 0:
			quotient = num % 2
			binaryStr = str(quotient) + binaryStr
			num = num / 2

		return binaryStr

	def reverseBits(self, num):
		binary = bin(num).split('b')[1]
		numZeros = 32 - len(binary)
		binary = '0' * numZeros + binary
		binary = binary[::-1]
		decimal = self.toDecimal(binary)
		return decimal


	def toDecimal(self, binary):
		decimal = 0
		numDigits = 0
		while len(binary) > 0:
			digit = binary[-1]
			decimal += pow(2, numDigits) * int(digit)
			binary = binary[:-1]
			numDigits += 1
		return decimal


if __name__ == "__main__":
	
	num = 2
	

	sol = Solution()
	print(sol.reverseBits(num))