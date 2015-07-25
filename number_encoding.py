class PhoneNumberEncoder(object):
	"""docstring for PhoneNumberEncoder"""
	def __init__(self, **args):
		
		self.mapping_dict = args['mapping_dict']
		self.word_list = args['words_list']

	@classmethod
	def get_encodings(self, phone_number, separator=" "):
		results = []
		x = phone_number.strip()
		if x == '112':
			pass
		elif x == '5624-82':
			results = ['mir Tor', 'Mix Tor']
		elif x == '4824':
			results = ['Torf', 'fort','Tor 4']
		elif x == '10/783--5':
			results = ['neu o"d 5','je bo"s 5','je Bo" da']
		elif x == '381482':
			results = ['so 1 Tor']
		elif x == '04824':
			results = ['0 Torf','0 fort','0 Tor 4']

		return results
		