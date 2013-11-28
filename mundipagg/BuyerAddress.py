class BuyerAddress:
	"""Class that represents a Buyer address"""


	class AddressTypeEnum: 
		"""Address Type Enum"""
		Billing = 'Billing'
		Shipping = 'Shipping'
		Work = 'Comercial'
		Home = 'Residential'

	class CountryEnum: 
		"""Country Enum"""
		Brazil = 'Brazil'
		UnitedStates = 'USA'
		Argentina = 'Argentina'
		Bolivia = 'Bolivia'
		Chile = 'Chile'
		Colombia = 'Colombia'
		Uruguay = 'Uruguay'
		Mexico = 'Mexico'
		Paraguay = 'Paraguay'			
	
	def __init__(self):
		# Address type [String]
		self.addressTypeEnum = self.AddressTypeEnum.Home

		# City [String]
		self.city = None

		# Address complement [String]
		self.complement = None

		# Address Country
		self.contryEnum = self.CountryEnum.Brazil

		# District [String]
		self.district = None

		# Address number [String]
		self.number = None

		# Address State [String]
		self.state = None

		# Street [String]
		self.street = None

		# Zip Code [String]
		self.zipCode = None	
		