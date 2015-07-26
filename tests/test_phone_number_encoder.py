import unittest
from number_encoding import PhoneNumberEncoder
from utils import create_mapping_dict, template
from mocks import sample_dictionary, sample_phones, correct_output
import logging

class TestNumberEncodings(unittest.TestCase):

    def setUp(self):
        mapping_dict = create_mapping_dict("E | J N Q | R W X | D S Y | F T | A M | C I V | B K U | L O P | G H Z")
        words_list = sample_dictionary
        self.phone_number_encoder = PhoneNumberEncoder(mapping_dict=mapping_dict, words_list=words_list)

    def test_correct_encoding_on_sample_data(self):
        expected_results = [s.strip() for s in correct_output]

        for phone_number in sample_phones:
            encodings = self.phone_number_encoder.get_encodings(phone_number, separator=" ")
            for encoding in encodings:
                expected_output = template(phone_number, encoding)
                assert expected_output in expected_results
                expected_results.remove(expected_output)
        logging.info('here expected_results should be empty %s' % expected_results)
        assert len(expected_results) == 0

    def test_empty_list_returned_when_no_encoding_found(self):
        assert len(self.phone_number_encoder.get_encodings('112')) == 0

    def test_returns_original_word_after_encoding(self):
        # 10/783--5: je Bo" da
        number = '1078'
        assert 'je Bo"' in self.phone_number_encoder.get_encodings(number)

    def test_ignore_extra_characters_when_encoding(self):
        weird_number = '//////----1---0/783--5'
        result1 = self.phone_number_encoder.get_encodings(weird_number)
        number = '107835'
        result2 = self.phone_number_encoder.get_encodings(number)
        assert result2 == result1

    def test_ensure_separator_is_respected(self):
        n = '10781078'
        res = self.phone_number_encoder.get_encodings(n, separator=' ')
        res2 = self.phone_number_encoder.get_encodings(n, separator='**')
        assert len(''.join(res).split(' ')) == len(''.join(res2).split('**'))



class TestNumberEncodingsRealData(unittest.TestCase):
    """docstring for TestNumberEncodingsRealData"""
    def setUp(self):
        mapping_dict = create_mapping_dict("E | J N Q | R W X | D S Y | F T | A M | C I V | B K U | L O P | G H Z")
        with open('dictionary.txt') as f:
            words_list = f.read().splitlines()
        self.phone_number_encoder = PhoneNumberEncoder(mapping_dict=mapping_dict, words_list=words_list)
        
    def test_empty_list_returned_when_no_encoding_found(self):
        assert len(self.phone_number_encoder.get_encodings('112')) == 0

    def test_get_encodings_with_big_dictionary(self):
        phone_number = "3202371835"

        result = self.phone_number_encoder.get_encodings(phone_number, separator=" ")
        assert result == ['3 wer du Jod 5', '3 wer du Joy 5']

    def test_encode_the_longest_word_in_dict(self):
        phone_number = '9316357348230213'
        result = self.phone_number_encoder.get_encodings(phone_number)
        assert 'zynismusfo"rdernd' in result

    def test_length_of_encoding_matches_length_of_number(self):
        phone_number = '68376528763907524156749871524386598025368689254638'
        # ignoring doublequotes, dashes and empty spaces the length of each result should match 
        # the length of the number
        result = self.phone_number_encoder.get_encodings(phone_number)
        assert all([ len(phone_number) == len(r.translate(None, ' "-')) for r in result])

    def test_50_longest_encodable_numbers_are_encoded(self):
        for phone_number in TOP_LONGEST_ENCODABLE_NUMBERS:
            result = self.phone_number_encoder.get_encodings(phone_number)
            assert len(phone_number) in [len(x.translate(None, '"-')) for x in result]

if __name__ == '__main__':
    unittest.main()