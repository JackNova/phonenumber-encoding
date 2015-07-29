import argparse
from number_encoding import PhoneNumberEncoder
from utils import create_mapping_dict, template
import io
import re
import sys

DEFAULT_MAPPING_DICT = "E | J N Q | R W X | D S Y | F T | A M | C I V | B K U | L O P | G H Z"

def parse_args(args=None):
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

	return parser.parse_args(args)

if sys.argv[0]:
	args = parse_args(args=sys.argv[1:])
else:
	args = parse_args()


def create_word_list(path):
	with open(path) as f:
		words_list = f.read().splitlines()
	return words_list


def run(words_list=create_word_list(args.d), source_stream=io.open(args.i, 'r')):
	mapping_dict = create_mapping_dict(args.m)
	phone_number_encoder = PhoneNumberEncoder(mapping_dict=mapping_dict, words_list=words_list)

	for phone_number in source_stream:
		safe_phone_number = ''.join(re.findall(r'\d+', phone_number))
		if phone_number == '':
			break
		elif len(safe_phone_number) < 2:
			continue
		else:
			result = phone_number_encoder.get_encodings(str(safe_phone_number))
			for r in result:
				print template(phone_number, r)
		

if __name__ == "__main__":
	run()
