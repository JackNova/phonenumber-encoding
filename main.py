import argparse
from number_encoding import PhoneNumberEncoder
from utils import create_mapping_dict, template
import io

DEFAULT_MAPPING_DICT = "E | J N Q | R W X | D S Y | F T | A M | C I V | B K U | L O P | G H Z"

parser = argparse.ArgumentParser(description='Encode phone numbers into list of words given a dictionary list and an encoding map')

parser.add_argument('--d',
	metavar='dictionary_path',
	type=str,
	help='path to the dictionary list',
	default='dictionary.txt')

parser.add_argument('--m',
	metavar='mapping',
	type=str,
	help='encoding map number => character',
	default=DEFAULT_MAPPING_DICT)

parser.add_argument('--i',
	metavar= 'src',
	type=str,
	help='source file containing one number on each line',
	default='numbers.txt')

args = parser.parse_args()

mapping_dict = create_mapping_dict(args.m)
with open(args.d) as f:
	words_list = f.read().splitlines()
phone_number_encoder = PhoneNumberEncoder(mapping_dict=mapping_dict, words_list=words_list)


with io.open(args.i, 'r') as source:
	while True:
		phone_number = source.readline()
		if not phone_number:
			break
		else:
			result = phone_number_encoder.get_encodings(str(phone_number))
			for r in result:
				print template(phone_number, r)

