class BoletoTransaction:

	def __init__(self):
		# Transaction amount in cents
		self.amountInCents = 0

		# Bank code
		self.bankNumber = None

		# How many days after the creation the boleto will be valid
		self.daysToAddInBoletoExpirationDate = 7

		# Number used to identify the boleto
		self.nossoNumero = None

		# Text with payment instructio. Limit: 120 characteres
		self.instructions = None

		# Custom transaction identifier
		self.transactionReference = None		