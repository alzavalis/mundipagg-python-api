import xml.etree.ElementTree as parser
from cStringIO import StringIO
from suds.client import Client
import logging

class Gateway:

	WEBSERVICE_TEST_URL = None    
	WEBSERVICE_PRODUCTION_URL = None

	def __init__(self,environment="test"):
		self.WEBSERVICE_TEST_URL = "https://transaction.mundipaggone.com/MundiPaggService.svc?wsdl"    
		self.WEBSERVICE_PRODUCTION_URL = "https://transaction.mundipaggone.com/MundiPaggService.svc?wsdl"
		self.environment = environment 

		logging.basicConfig(level=logging.INFO)
		logging.getLogger('suds.client').setLevel(logging.DEBUG)
		#logging.getLogger('suds.transport').setLevel(logging.DEBUG)

	def getUrl(self):
		url = None	

		if self.environment == "production":
			url = self.WEBSERVICE_PRODUCTION_URL
		else:
			url = self.WEBSERVICE_TEST_URL

		return url

	def ManageOrder(self,request):
		url = self.getUrl()

		client = Client(url)		

		ManageCreditCardTransactionRequest = []

		manageOrderRequest = client.factory.create('ns0:ManageOrderRequest')
		arrayOfManageCreditCardTransactionRequest = client.factory.create('ns0:ArrayOfManageCreditCardTransactionRequest')
				
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

		arrayOfManageCreditCardTransactionRequest = ManageCreditCardTransactionRequest

		manageOrderRequest.ManageCreditCardTransactionCollection = arrayOfManageCreditCardTransactionRequest
		manageOrderRequest.ManageOrderOperationEnum = request.manageOrderOperationEnum.Capture


		print manageOrderRequest

		result = client.service.ManageOrder(manageOrderRequest)
		print result

	def QueryOrder(self,request):
		url = self.getUrl()

		client = Client(url)

		queryOrderRequest = client.factory.create('ns0:QueryOrderRequest')

		queryOrderRequest.MerchantKey = request.merchantKey
		queryOrderRequest.OrderKey = request.orderKey
		queryOrderRequest.OrderReference = request.orderReference
		queryOrderRequest.RequestKey = request.requestKey

		result = client.service.QueryOrder(queryOrderRequest)

	def CreateOrder(self,request):
		url = self.getUrl()

		client = Client(url)

		createOrderRequest = client.factory.create('ns0:CreateOrderResponse')

		createOrderRequest.AmountInCents = request.amountInCents
		createOrderRequest.AmountInCentsToConsiderPaid = request.amountInCentsToConsiderPaid
		createOrderRequest.CurrencyIsoEnum = request.currencyIsoEnum
		createOrderRequest.MerchantKey = request.merchantKey
		createOrderRequest.OrderReference = request.orderReference
		createOrderRequest.RequestKey = request.requestKey

		if request.buyer is None:
			createOrderRequest.Buyer = request.buyer
		else:
			createOrderRequest.Buyer = self.CreateBuyer(request)

		if request.creditCardTransactionCollection is not None and request.creditCardTransactionCollection.count > 0:
			creditCardTransactionCollection = self.CreateCreditCardTransaction(request)
			createOrderRequest.CreditCardTransactionCollection = creditCardTransactionCollection
		else:
			createOrderRequest.CreditCardTransactionCollection = None

		if request.boletoTransactionCollection is not None and request.boletoTransactionCollection.count > 0:
			boletoTransactionCollection = self.CreateBoletoTransactionRequest(request)
			createOrderRequest.BoletoTransactionCollection = boletoTransactionCollection
		else:
			createOrderRequest.BoletoTransactionCollection = None

		result = client.service.CreateOrder(createOrderRequest)

	def CreateBuyer(self,request):
		url = self.getUrl()

		client = Client(url)

		buyer = client.factory.create('ns0:Buyer')

		buyer.BuyerKey = request.buyer.buyerKey
		buyer.BuyerReference = request.buyer.buyerReference
		buyer.Email = request.buyer.email
		buyer.FacebookId = request.buyer.facebookId
		buyer.GenderEnum = request.buyer.genderEnum
		buyer.HomePhone = request.buyer.homePhone
		buyer.IpAddress = request.buyer.ipAddress
		buyer.MobilePhone = request.buyer.mobilePhone
		buyer.Name = request.buyer.name
		buyer.PersonTypeEnum = request.buyer.personTypeEnum
		buyer.TaxDocumentNumber = request.buyer.taxDocumentNumber
		buyer.TaxDocumentTypeEnum = request.buyer.taxDocumentTypeEnum
		buyer.WorkPhone = request.buyer.workPhone
		buyer.BuyerAddressCollection = request.buyer.buyerAddressCollection

		return buyer

	def CreateBoletoTransactionRequest(self,request):
		url = self.getUrl()

		client = Client(url)

		transactionCollection = []

		boletoTransactionRequest = client.factory.create('ns0:BoletoTransaction')

		for boleto in request.boletoTransactionCollection:
			boletoTransactionRequest.AmountInCents = boleto.amountInCents
			boletoTransactionRequest.BankNumber = boleto.bankNumber
			boletoTransactionRequest.DaysToAddInBoletoExpirationDate = boleto.daysToAddInBoletoExpirationDate
			boletoTransactionRequest.Instructions = boleto.instructions
			boletoTransactionRequest.NossoNumero = boleto.nossoNumero
			boletoTransactionRequest.TransactionReference = boleto.transactionReference

			transactionCollection.append(boletoTransactionRequest)

		return boletoTransactionRequest		

	#TODO
	def CreateCreditCardTransaction(self,request):
		url = self.getUrl()

		client = Client(url)

		transactionCollection = []

		creditCardTransaction = client.factory.create('ns0:CreditCardTransaction')

		for transaction in request.creditCardTransactionCollection:
			creditCardTransaction.AmountInCents = None
			creditCardTransaction.CaptureDelayInMinutes = None
			creditCardTransaction.CreditCardBrandEnum =(CreditCardBrandEnum){value = None   }
			creditCardTransaction.CreditCardNumber = None
			creditCardTransaction.CreditCardOperationEnum =(CreditCardOperationEnum){value = None}
			creditCardTransaction.ExpMonth = None
			creditCardTransaction.ExpYear = None
			creditCardTransaction.HolderName = None
			creditCardTransaction.IataAmountInCents = None
			creditCardTransaction.InstallmentCount = None
			creditCardTransaction.InstantBuyKey = None
			creditCardTransaction.PaymentMethodCode = None
			creditCardTransaction.SecurityCode = None
			creditCardTransaction.ThirdPartyMerchantKey = None
			creditCardTransaction.TransactionReference = None

			creditCardTransaction.Recurrency.DateToStartBilling = transaction.recurrency.dateToStartBilling
			creditCardTransaction.Recurrency.FrequencyEnum = transaction.recurrency.frequencyEnum
			creditCardTransaction.Recurrency.Interval = transaction.recurrency.interval
			creditCardTransaction.Recurrency.OneDollarAuth = transaction.recurrency.oneDollarAuth
			creditCardTransaction.Recurrency.Recurrences = transaction.recurrency.recurrences

			transactionCollection.append(creditCardTransaction)

		return transactionCollection



