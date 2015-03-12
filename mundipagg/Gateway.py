from cStringIO import StringIO
from suds.client import Client
import logging

class Gateway:
	"""Class responsable for comunicating with the service via SOAP"""

	def __init__(self,environment="test"):
		self.WEBSERVICE_TEST_URL = "https://transaction.mundipaggone.com/MundiPaggService.svc?wsdl"
		self.WEBSERVICE_PRODUCTION_URL = "https://transaction.mundipaggone.com/MundiPaggService.svc?wsdl"
		self.environment = environment

		logging.basicConfig(level=logging.INFO)
		logging.getLogger('suds.client').setLevel(logging.DEBUG)
		#logging.getLogger('suds.transport').setLevel(logging.DEBUG)

	def getUrl(self):
		"""Decides with URL to use based in the environment value

	    :returns: URL string
	    """
		url = None

		if self.environment == "production":
			url = self.WEBSERVICE_PRODUCTION_URL
		else:
			url = self.WEBSERVICE_TEST_URL

		return url

	def CreateBuyer(self,request):
		"""This method creates an CreateBuyer object

	    :param request: A CreateOrderRequest
	    :returns: Buyer object
	    """
		url = self.getUrl()

		client = Client(url)

		buyer = client.factory.create('ns0:Buyer')

		buyerAddress = client.factory.create('ns0:BuyerAddress')

		addressCollection = []

		for address in request.buyer.addressCollection:
			buyerAddress.AddressTypeEnum = address.addressTypeEnum
			buyerAddress.City = address.city
			buyerAddress.Complement = address.complement
			buyerAddress.CountryEnum = address.countryEnum
			buyerAddress.District = address.district
			buyerAddress.Number = address.number
			buyerAddress.State = address.state
			buyerAddress.Street = address.street
			buyerAddress.ZipCode = address.zipCode

			addressCollection.append(buyerAddress)

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
		buyer.BuyerAddressCollection = addressCollection

		return buyer

	def CreateBoletoTransaction(self,request):
		"""This method creates an CreateBoletoTransaction object

	    :param request: A CreateOrderRequest
	    :type request: CreateOrderRequest
	    :returns: BoletoTransaction object
	    """
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



	def CreateCreditCardTransaction(self,request):
		"""This method creates an CreateCreditCardTransaction object

	    :param request: A CreateOrderRequest
	    :type request: CreateOrderRequest
	    :returns: CreateCreditCardTransaction object
	    """

		url = self.getUrl()

	 	client = Client(url)

	 	transactionCollection = []

	 	creditCardTransactionCollection = client.factory.create('ns0:ArrayOfCreditCardTransaction')

	 	creditCardTransaction = client.factory.create('ns0:CreditCardTransaction')

	 	for transaction in request.creditCardTransactionCollection:
	 		creditCardTransaction.AmountInCents = transaction.amountInCents
	 		creditCardTransaction.CreditCardBrandEnum = transaction.creditCardBrandEnum
	 		creditCardTransaction.CreditCardNumber = transaction.creditCardNumber
	 		creditCardTransaction.CreditCardOperationEnum = transaction.creditCardOperationEnum
	 		creditCardTransaction.ExpMonth = transaction.expirationMonth
	 		creditCardTransaction.ExpYear = transaction.expirationYear
	 		creditCardTransaction.HolderName = transaction.holderName
	 		creditCardTransaction.InstallmentCount = transaction.installmentCount
	 		creditCardTransaction.PaymentMethodCode = transaction.paymentMethodCode
	 		creditCardTransaction.SecurityCode = transaction.securityCode
	 		creditCardTransaction.TransactionReference = transaction.transactionReference

	 		if transaction.recurrency is not None:
		 		creditCardTransaction.Recurrency.DateToStartBilling = transaction.recurrency.dateToStartBilling
		 		creditCardTransaction.Recurrency.FrequencyEnum = transaction.recurrency.frequencyEnum
		 		creditCardTransaction.Recurrency.Interval = transaction.recurrency.interval
		 		creditCardTransaction.Recurrency.OneDollarAuth = transaction.recurrency.oneDollarAuth
		 		creditCardTransaction.Recurrency.Recurrences = transaction.recurrency.recurrences

	 		transactionCollection.append(creditCardTransaction)

	 	creditCardTransactionCollection.CreditCardTransaction = transactionCollection

	 	return creditCardTransactionCollection


	def ManageOrder(self,request):
		"""Calls the ManageOrder method

		:param request: An CreateOrderRequest
		"""
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
		manageOrderRequest.ManageOrderOperationEnum = request.operationEnum.Capture

		result = client.service.ManageOrder(manageOrderRequest)

		return result

	def QueryOrder(self,request):
		"""Calls the QueryOrder method

	    :param request: A QueryOrderRequest
	    """
		url = self.getUrl()

		client = Client(url)

		queryOrderRequest = client.factory.create('ns0:QueryOrderRequest')

		queryOrderRequest.MerchantKey = request.merchantKey
		queryOrderRequest.OrderKey = request.orderKey
		queryOrderRequest.OrderReference = request.orderReference
		queryOrderRequest.RequestKey = request.requestKey

		result = client.service.QueryOrder(queryOrderRequest)

		return result

	def CreateOrder(self,request):
		"""Calls the CreateOrder method

	    :param request: A CreateOrderRequest
	    """
		url = self.getUrl()

		client = Client(url)

		createOrderRequest = client.factory.create('ns0:CreateOrderRequest')

		print createOrderRequest

		createOrderRequest.AmountInCents = request.amountInCents
		createOrderRequest.AmountInCentsToConsiderPaid = request.amountInCentsToConsiderPaid
		createOrderRequest.CurrencyIsoEnum = request.currencyIsoEnum
		createOrderRequest.MerchantKey = request.merchantKey
		createOrderRequest.OrderReference = request.orderReference
		createOrderRequest.RequestKey = request.requestKey
		createOrderRequest.EmailUpdateToBuyerEnum = request.emailUpdateToBuyerEnum

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
			boletoTransactionCollection = self.CreateBoletoTransaction(request)
			createOrderRequest.BoletoTransactionCollection = boletoTransactionCollection
		else:
			createOrderRequest.BoletoTransactionCollection = None

		result = client.service.CreateOrder(createOrderRequest)

		return result
