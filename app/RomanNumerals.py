import sys

class RomanNumerals(object):

	def userConvert(self, x):
		try:
			return self.convertToRoman(x)
			
		except (Exception) as err:
			sys.stderr.write('ERROR: %s' % str(err))

	def convertToRoman(self, x):
				
		romanString = ''
		romanValues = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
		romanChars = ["M", "CM","D","CD","C", "XC", "L", "XL", "X","IX","V","IV","I"]

		try:
			userValue = int(x)
		except:
			raise ValueError("Not a valid integer")
		
		if userValue > 0 and userValue < 4000:
			for i in range(0, len(romanValues)):
				while userValue%romanValues[i]<userValue:
					romanString += romanChars[i]
					userValue -= romanValues[i]

			return romanString
		else:
			raise ValueError("Value out of range (1-3999)")