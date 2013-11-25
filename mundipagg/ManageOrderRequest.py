class ManageOrderRequest:

	class OperationEnum:
		Capture = 'Capture'
		Void = 'Void'
			
	
	def __init__(self):
		self.transactionCollection = []		
		self.manageOrderOperationEnum = self.OperationEnum
		self.merchantKey = None
		self.orderKey = None
		self.orderReference	= None
		self.requestKey	= '00000000-0000-0000-0000-000000000000'
		#self.operationEnum = self.OperationEnum

	class ManageTransactionRequest:

		def __init__(self):
			amountInCents = None
			transactionKey = None
			transactionReference = None
													