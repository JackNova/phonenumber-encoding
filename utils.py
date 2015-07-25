def create_mapping_dict(s):
	""" imput string format: "E | J N Q | R W X | D S Y | F T | A M | C I V | B K U | L O P | G H Z"
		where each pipe signals the next corresponding number starting from zero"""
	result = {}
	for index, chars in enumerate(s.upper().split('|')):
	    for c in chars.strip().split(' '):
	        result[c] = index
	        
	return result

def template(phone_number, encoding):
	return "%s: %s" % (phone_number.strip(), encoding.strip())