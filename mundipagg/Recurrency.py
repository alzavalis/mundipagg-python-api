class Recurrency:

	class Frequency:
		Monthly = 'Monthly'
		Yearly = 'Yearly'
		Daily = 'Daily'

	
	def __init__(self):
		self.dateToStartBilling = None
		self.frequencyEnum = self.Frequency
		self.interval = None
		self.oneDollarAuth = None
		self.recurrences = None		