class Index(object):
	"""docstring for LookupByLenghtAdnEncoding"""
	def __init__(self, **kwargs):
		self.associated_number =  kwargs['mapping_dict']
		self.words_list = [w.strip() for w in kwargs['words_list'] if w is not '']
		self.build_index()

	def encode_word(self, word):
		return ''.join([str(self.associated_number[char.upper()]) for char in word.translate(None, '"-')])

	def build_index(self):
		self.index = {}
		for word in self.words_list:
			encoded = self.encode_word(word)
			if encoded not in self.index:
				self.index[encoded] = []
			
			self.index[encoded].append(word)

	def lookup(self, number):
		return self.index.get(number, None)

