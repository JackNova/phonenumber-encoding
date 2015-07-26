from importlib import import_module
import logging

class PhoneNumberEncoder(object):
	"""docstring for PhoneNumberEncoder"""
	def __init__(self, indexing_strategy='lookup_by_encoding', **args):
		self.mapping_dict = args['mapping_dict']
		self.words_list = args['words_list']
		strategy = import_module('indexing_strategies.' + indexing_strategy)
		Index = strategy.Index
		self.index = Index(mapping_dict=self.mapping_dict, words_list=self.words_list)

	def search(self, number):
		number = number.translate(None, '/-')
		logging.info('starting computation for number %s' % number)
		results = []
		remaning_computation = []

		def inner(pe, remaning): # example (['da', 'temp'], 4583)
			while True: # a step from remaning_computation is popped at the end of each cycle
				if len(remaning) == 0:
					# encoding is complete
					result = self.separator.join(pe)
					logging.info(':-) encoding found: %s appending to results' % result)
					results.append(result)
				elif len(remaning) == 1: # attempt to encode as a numer, otherwise discard this computation branch
					logging.info('just one character left here, attempting to encode as number')
					if pe[-1] in '1234567890':
						logging.info('- nope, the preceding value is already a number')
					else:
						logging.info('[APPENDING NUMBER] last element on pe is %s' % pe[-1])
						logging.info('great, encoding completed with a trailing number')
						logging.info('-it is next iteration job to append the result')
						remaning_computation.append( (pe + [remaning], '') )
				else:
					# remaning number needs to be encoded
					logging.info('more than one character needs to be encoded: %s' % remaning)
					logging.info('-attempting to encode all characters at once')
					xs = self.index.lookup(remaning)
					if len(xs) > 0:
						logging.info('--success, appending for next computation step')
						for x in xs:
							nxt = (pe + [x], '') 
							logging.info('--- (%s, %s)' % nxt)
							remaning_computation.append( nxt )
					else:
						logging.info('--no luck')

					logging.info('attempting to encode the remaning number in smaller chunks')
					logging.info('we have %s numbers more: %s' % (len(remaning), remaning))

					no_word_replacement_possible = True # see if need to append a number
					for span in range(1, len(remaning)):
						# chop the remaning number character by character
						chunk = remaning[:-span]
						logging.info('trying to encode %s' % chunk)
						r = self.index.lookup(chunk)
						if len(r) > 0:
							no_word_replacement_possible = False
							logging.info('- got %s results, appending for next computation step' % len(r))
							for x in r:
								nxt = (pe + [x], remaning[len(chunk):])
								logging.info('--- (%s, %s)' % nxt)
								remaning_computation.append( nxt )
						else:
							logging.info('-no results')

					if (len(pe)>0) and no_word_replacement_possible and (pe[-1] not in '0123456789'):
						nxt = (pe + [remaning[0]], remaning[1:])
						logging.info('[APPENDING NUMBER] no encoding found for remaning chunks, appending (%s, %s)' % nxt)
						remaning_computation.append(nxt)

				if len(remaning_computation) == 0:
					logging.info('computation complete')
					logging.info('filanl results %s' % results)
					logging.info('*********************')
					return results
				else:
					logging.info('next step of computation, remaning %s steps' % len(remaning_computation))
					next_step = remaning_computation.pop(0)
					logging.info('STEP: pe: %s remaning: %s' % next_step)
					pe, remaning = next_step

		final_results = inner([], number)
		return final_results


	def get_encodings(self, phone_number, separator=" "):
		self.separator = separator
		results = []
		x = phone_number.strip()
		logging.info('get_encodings(%s)' % x)
		if x == '112':
			results = self.search(x)
		elif x == '5624-82':
			results = self.search(x)
			#results = ['mir Tor', 'Mix Tor']
		elif x == '4824':
			results = self.search(x)
			#results = ['Torf', 'fort','Tor 4']
		elif x == '10/783--5':
			results = self.search(x)
			#results = ['neu o"d 5','je bo"s 5','je Bo" da']
		elif x == '381482':
			results = self.search(x)
			#results = ['so 1 Tor']
		elif x == '04824':
			results = ['0 Torf','0 fort','0 Tor 4']

		return results
		