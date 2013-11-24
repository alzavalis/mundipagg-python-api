class Buyer(object):	

	class GenderEnum(object):
		Male = 'M'
		Female = 'F'

	class PersonTypeEnum(object):
		Person = 'Person'
		Company = 'Company'

	class DocumentType(object):
		CPF = 'CPF'
		CNPJ = 'CNPJ'
	
	def __init__(self):		
		self.buyerReference 		= None
		self.email 					= None
		self.facebookId 			= None
		self.genderEnum 			= None
		self.homePhone 				= None
		self.ipAddress 				= None
		self.mobilePhone 			= None
		self.workPhone 				= None
		self.name 					= None		
		self.taxDocumentNumber 		= None		
		self.twitterId 				= None		
		self.addressCollection 		= []
		self.buyerKey 				= '00000000-0000-0000-0000-000000000000'
		self.PersonTypeEnum 		= self.PersonTypeEnum.Person
		self.taxDocumentTypeEnum 	= self.DocumentType.CPF