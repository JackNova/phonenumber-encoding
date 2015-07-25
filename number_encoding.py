class PhoneNumberEncoder(object):
	"""docstring for PhoneNumberEncoder"""
	def __init__(self, **args):
		
		self.mapping_dict = args['mapping_dict']
		self.word_list = args['words_list']

	@classmethod
	def get_encodings(self, phone_number, separator=" "):
		results = []
		return results
		