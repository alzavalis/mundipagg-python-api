import sys
import uuid
sys.path.append('C:\\Users\\agaldino\\Documents\\mundipagg-python-api')

from mundipagg import BoletoTransaction
from mundipagg import Buyer
from mundipagg import BuyerAddress
from mundipagg import CreateOrderRequest
from mundipagg import CreditCardTransaction
from mundipagg import BoletoTransaction
from mundipagg import QueryOrderRequest

def newBoletoTransaction():
	"""Creates a fake BoletoTransaction

	:returns: BoletoTransaction object
	"""
	boletoTransaction = BoletoTransaction.BoletoTransaction()

	boletoTransaction.amountInCents = 10
	boletoTransaction.bankNumber = 314	
	boletoTransaction.nossoNumero = 321654
	boletoTransaction.instructions = None

	return boletoTransaction

def newBuyerAddress():
	"""Creates a fake BuyerAddress

	:returns: BuyerAddress object
	"""
	buyerAddress = BuyerAddress.BuyerAddress()
	
	buyerAddress.city = 'Rio de Janeiro'
	buyerAddress.complement = '01'
	buyerAddress.number = '08'
	buyerAddress.district = 'Bangu'
	buyerAddress.state = 'Rio de Janeiro'
	buyerAddress.street = 'Rua dos bobos '
	buyerAddress.zipCode = '21382145'	

	return buyerAddress

def newBuyer():
	"""Creates a fake Buyer

	:returns: Buyer object
	"""
	buyer = Buyer.Buyer()

	buyer.buyerReference = '1'
	buyer.email = 'marvin@universe.com'	
	buyer.homePhone = '+55(021)12345678'
	buyer.ipAddress = '127.0.0.1'
	buyer.mobilePhone = '+55(021)12345678'
	buyer.workPhone = '+55(021)12345678'
	buyer.name = 'Marvin'		
	buyer.taxDocumentNumber = '00000000000'
	buyer.addressCollection.append(newBuyerAddress())


	return buyer

def newCreditCardTransaction():
	"""Creates a fake CreditCardTransaction

	:returns: CreditCardTransaction object
	"""
	creditCardTransaction = CreditCardTransaction.CreditCardTransaction()

	creditCardTransaction.amountInCents = 10
	creditCardTransaction.creditCardBrandEnum = creditCardTransaction.brandEnum.MasterCard
	creditCardTransaction.creditCardNumber = '3214654498773211'
	creditCardTransaction.creditCardOperationEnum = creditCardTransaction.operationEnum.AuthOnly
	creditCardTransaction.expirationMonth = 12
	creditCardTransaction.expirationYear = 2014
	creditCardTransaction.holderName = 'Marvin the Android Paranoid'
	creditCardTransaction.installmentCount = 1
	creditCardTransaction.securityCode = 456
	creditCardTransaction.paymentMethodCode = 1
	creditCardTransaction.transactionReference = 'transactionReference'
	

	return creditCardTransaction


def newCreateOrderRequest():
	"""Creates a fake CreateOrderRequest

	:returns: CreateOrderRequest object
	"""
	createOrderRequest = CreateOrderRequest.CreateOrderRequest()

	createOrderRequest.amountInCents = 10
	createOrderRequest.amountInCentsToConsiderPaid = 0	
	createOrderRequest.buyer = '1'
	createOrderRequest.merchantKey = uuid.uuid1()
	createOrderRequest.orderReference = 'Order 42'
	createOrderRequest.creditCardTransactionCollection.append(newCreditCardTransaction())
	createOrderRequest.boletoTransactionCollection.append(newBoletoTransaction())

	return createOrderRequest

def newQueryOrderRequest():
	"""Creates a fake QueryOrderRequest

	:returns: QueryOrderRequest object
	"""
	queryOrderRequest = QueryOrderRequest.QueryOrderRequest()

	self.merchantKey = uuid.uuid1()
	self.orderKey = uuid.uuid1()
	self.orderReference = 'Order 42'
	self.requestKey = uuid.uuid1()


	return queryOrderRequest