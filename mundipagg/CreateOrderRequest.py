class CreateOrderRequest:	

	class CurrencyIsoEnum:
		BrazillianReal = 'BRL'
		AmericanDollar = 'USD'

	def __init__(self):
		self.amountInCents = None
		self.amountInCentsToConsiderPaid = None
		self.currencyIsoEnum = self.CurrencyIsoEnum.BrazillianReal
		self.buyer = None
		self.merchantKey = None
		self.orderReference = None
		self.creditCardTransactionCollection = []
		self.boletoTransactionCollection = []
		self.requestkey = '00000000-0000-0000-0000-000000000000'