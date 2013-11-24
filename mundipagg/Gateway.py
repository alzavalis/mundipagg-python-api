import xml.etree.ElementTree as parser

class Gateway(object):

	
	def __init__(self):
		
	
	def ManageOrder(request):
		hash = parser.fromstring('''<tns:manageOrderRequest>
		                                    <mun:ManageCreditCardTransactionCollection>
		                                    </mun:ManageCreditCardTransactionCollection>
		                                    <mun:ManageOrderOperationEnum>?</mun:ManageOrderOperationEnum>
		                                    <mun:MerchantKey>?</mun:MerchantKey>
		                                    <mun:OrderKey>?</mun:OrderKey>
		                                    <mun:OrderReference>?</mun:OrderReference>
		                                    <mun:RequestKey>?</mun:RequestKey>
		                            </tns:manageOrderRequest>''')

		xml_hash = hash['<tns:manageOrderRequest']

		xml_hash['mun:ManageCreditCardTransactionCollection'] = {'mun:ManageCreditCardTransactionRequest' : []}

		if request.transactionCollection is None and request.transactionCollection.count > 0 :			
			pass
