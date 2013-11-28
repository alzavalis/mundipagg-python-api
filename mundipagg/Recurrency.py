class Recurrency:
	"""Class that hold recurrency transaction information"""

	class Frequency:
		Monthly = 'Monthly'
		Yearly = 'Yearly'
		Daily = 'Daily'

	
	def __init__(self):
		# Date the first recurrency will be charged [Date]
		self.dateToStartBilling = None

		# Indicating the recurrency frequency [String]
		self.frequencyEnum = self.Frequency

		# Recurrency interval [Integer]
		self.interval = None

		# Indicates whether the One webservice will run a OneDollarAuth [Boolean]
		self.oneDollarAuth = None

		# Number of recurrencies [Integer]
		self.recurrences = None		