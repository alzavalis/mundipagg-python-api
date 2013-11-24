class BuyerAddress(object):

	class AddressTypeEnum(object):
		Billing = 'Billing'
		Shipping = 'Shipping'
		Work = 'Comercial'
		Home = 'Residential'

	class CountryEnum(object):
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
		self.addressTypeEnum = self.AddressTypeEnum.Home
		self.city = None
		self.complement = None
		self.contryEnum = self.CountryEnum.Brazil
		self.district = None
		self.number = None
		self.state = None
		self.street = None
		self.zipCode = None	
		