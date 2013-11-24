class CreateOrderRequest(object):	

	class CurrencyIsoEnum(object):
		BrazillianReal = 'BRL'
		AmericanDollar = 'USD'

	def __init__(self, arg):
		self.amountInCents 						= None
		self.amountInCentsToConsiderPaid 		= None
		self.currencyIsoEnum 					= self.CurrencyIsoEnum.BrazillianReal
		self.buyer								= None
		self.merchantKey 						= None
		self.orderReference 					= None
		self.creditCardTransactionCollection 	= []
		self.boletoTransactionCollection 		= []
		self.requestkey 						= '00000000-0000-0000-0000-000000000000'