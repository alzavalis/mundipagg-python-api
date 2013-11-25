import xml.etree.ElementTree as parser
from cStringIO import StringIO
from suds.client import Client

class Gateway:

	WEBSERVICE_TEST_URL = None    
	WEBSERVICE_PRODUCTION_URL = None

	def __init__(self,environment="test"):
		self.WEBSERVICE_TEST_URL = "https://transaction.mundipaggone.com/MundiPaggService.svc?wsdl"    
		self.WEBSERVICE_PRODUCTION_URL = "https://transaction.mundipaggone.com/MundiPaggService.svc?wsdl"
		self.environment = environment

	def ManageOrder(self,request):
		url = self.getUrl()

		client = Client(url)		

		ManageCreditCardTransactionRequest = []

		manageOrderRequest = client.factory.create('ns0:ManageOrderRequest')	
				
		if request.transactionCollection is None and request.transactionCollection.count > 0 :

			for transaction in request.transactionCollection:
					ManageCreditCardTransactionRequest.append({
						 'AmountInCents' : transaction.amountInCents, 
						 'TransactionKey' : transaction.transactionKey,
	 					 'TransactionReference' : transaction.transactionReference 
					})
		
		manageOrderRequest.MerchantKey = request.merchantKey
		manageOrderRequest.OrderKey = request.orderKey
		manageOrderRequest.OrderReference = request.orderReference
		manageOrderRequest.RequestKey = request.requestKey

		manageOrderRequest.ArrayOfManageCreditCardTransactionRequest = ManageCreditCardTransactionRequest
		manageOrderRequest.ManageOrderOperationEnum.value = request.manageOrderOperationEnum.Capture

		print manageOrderRequest

		result = client.service.ManageOrder(manageOrderRequest)
		print result

	def getUrl(self):
		url = None	

		if self.environment == "production":
			url = self.WEBSERVICE_PRODUCTION_URL
		else:
			url = self.WEBSERVICE_TEST_URL

		return url