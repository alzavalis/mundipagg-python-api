class ManageOrderRequest(object):

	class OperationEnum(object):
		Capture = 'Capture'
		Void = 'Void'
			
	
	def __init__(self, arg):
		self.transactionCollection 		= []
		self.manageOrderOperationEnum	= None
		self.merchantkey 				= None
		self.orderkey 					= None
		self.orderReference				= None
		self.requestKey					= '00000000-0000-0000-0000-000000000000'
		self.operationEnum 				= self.OperationEnum

	class ManageTransactionRequest(object):

		def __init__():
			amountInCents 		 = None
			transactionKey 		 = None
			transactionReference = None
													