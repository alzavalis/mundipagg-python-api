class CreateOrderRequest:	

	class CurrencyIsoEnum:
		"""Currency Iso Enum"""
		BrazillianReal = 'BRL'
		AmericanDollar = 'USD'

	def __init__(self):
		# Order amount in cents [long]
		self.amountInCents = None

		# Amount (in cents) to consider the order paid
		self.amountInCentsToConsiderPaid = None

		# Order amount currency [String]
		self.currencyIsoEnum = self.CurrencyIsoEnum.BrazillianReal

		# Buyer instance
		self.buyer = None

		# Mundipagg merchant identification
		self.merchantKey = None

		# If merchant not send OrderReference, Mundipagg will generate and return in the response.
        # @return [String] Custom order identification.
		self.orderReference = None

		# list with all credit card transaction [List]
		self.creditCardTransactionCollection = []

		# List with all boleto transaction [List]
		self.boletoTransactionCollection = []

		# If not send, it will be generate automatically in the webservice and returned in response.
        # Web service request identification, it is used for investigate problems with webservice requests.
        # @return [Guid] Globally Unique Identifier. 		
		self.requestkey = '00000000-0000-0000-0000-000000000000'