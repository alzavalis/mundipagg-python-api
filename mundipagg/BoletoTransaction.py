class BoletoTransaction:
	"""Class that hold an BoletoTransaction information"""

	# Transaction amount in cents
	amountInCents = 0

	# Bank code
	bankNumber = None

	# How many days after the creation the boleto will be valid
	daysToAddInBoletoExpirationDate = None

	# Number used to identify the boleto
	nossoNumero = None

	# Text with payment instructio. Limit: 120 characteres
	instructions = None

	# Custom transaction identifier
	transactionReference = None

	def __init__(self):
		self.daysToAddInBoletoExpirationDate = 7		