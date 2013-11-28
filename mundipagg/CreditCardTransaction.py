class CreditCardTransaction:

	class BrandEnum:
		"""Credit card brand enum"""
		Visa = 'Visa'
		MasterCard = 'MasterCard'
		AmericanExpress = 'Amex'
		Hipercard = 'Hipercard'
		Diners = 'Diners'
		Elo = 'Elo'
		Aura = 'Aura'
		Discover = 'Discover'

	class OperationEnum:
		"""Operation type enum"""
		AuthOnly = 'AuthOnly'
		AuthAndCapture = 'AuthAndCapture'
		AuthAndCaptureDelay = 'AuthAndCaptureDelay'	


	def __init__(self):

		# Transaction amount in cents [Long]
		self.amountInCents = None

		# Card brand. Use the BrandEnum class [String]
		self.creditCardBrandEnum = None

		# Credit card number [String]
		self.creditCardNumber = None

		# Type of operation. User OperationEnum class [String]
		self.creditCardOperationEnum = None

		# Credit card expiration month [Integer]
		self.expirationMonth = None

		# Credit card expiration year [Integer]
		self.expirationYear = None

		# Name in the credit card [String]
		self.holderName = None

		# Transaction installments count [Integer]
		self.installmentCount = None

		# Card security code [Integer]
		self.securityCode = None

		# Code to select the payment method. Can be Cielo, Redecard and others [Integer]
		self.paymentMethodCode = None

		# Custom transaction identifier [String]
		self.transactionReference = None

		# Fill this property when creating a recurrency transaction. 
   		# [Recurrency] Transaction recurrency information.
		self.recurrency = None

		# Brand enum
		self.brandEnum = self.BrandEnum

		# Operation enum
		self.operationEnum = self.OperationEnum