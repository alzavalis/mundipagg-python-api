class CreditCardTransaction:

	class BrandEnum:
		Visa = 'Visa'
		MasterCard = 'MasterCard'
		AmericanExpress = 'Amex'
		Hipercard = 'Hipercard'
		Diners = 'Diners'
		Elo = 'Elo'
		Aura = 'Aura'
		Discover = 'Discover'

	class OperationEnum:
		AuthOnly = 'AuthOnly'
		AuthAndCapture = 'AuthAndCapture'
		AuthAndCaptureDelay = 'AuthAndCaptureDelay'	


	def __init__(self):
		self.amountInCents = None
		self.creditCardBrandEnum = None
		self.creditCardNumber = None
		self.creditCardOperationEnum = None
		self.expirationMonth = None
		self.expirationYear = None
		self.holderName = None
		self.installmentCount = None
		self.securityCode = None
		self.paymentMethodCode = None
		self.transactionReference = None
		self.recurrency = None			
		self.brandEnum = self.BrandEnum
		self.operationEnum = self.OperationEnum