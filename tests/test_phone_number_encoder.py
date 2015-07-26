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


if __name__ == '__main__':
    unittest.main()