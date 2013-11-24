import xml.etree.ElementTree as parser
from cStringIO import StringIO

class Gateway:

	def __init__(self):
		pass

	def ManageOrder(self,request):
				
		self.ManageOrderXML = '''<manageOrderRequest>
		                                    <ManageCreditCardTransactionCollection>
		                                    </ManageCreditCardTransactionCollection>
		                                    <ManageOrderOperationEnum>1000</ManageOrderOperationEnum>
		                                    <MerchantKey>?</MerchantKey>
		                                    <OrderKey>?</OrderKey>
		                                    <OrderReference>?</OrderReference>
		                                    <RequestKey>?</RequestKey>
		                         </manageOrderRequest>'''

		print self.ManageOrderXML
		
		tree = parser.parse(StringIO(self.ManageOrderXML))
		root = root.getroot()
				
		for element in root:
			print element.tag, element.attrib, element.text

		root.find('ManageCreditCardTransactionCollection').text = str({'ManageCreditCardTransactionRequest' : []})

		# if request.transactionCollection is None and request.transactionCollection.count > 0 :			
			
		# 	for transaction in request.transactionCollection:
		# 		root.find('ManageCreditCardTransactionRequest') << {
		# 			 'AmountInCents' : transaction.amountInCents, 
		# 			 'TransactionKey' : transaction.transactionKey, 
		# 			 'TransactionReference' : transaction.transactionReference 
		# 		}


		root.find('ManageOrderOperationEnum').text = request.manageOrderOperationEnum
		root.find('MerchantKey').text = request.merchantKey
		root.find('OrderKey').text = request.orderKey
		root.find('OrderReference').text = request.orderReference
		root.find('RequestKey').text = request.requestKey

		for element in root:
			print element.tag, element.attrib, element.text