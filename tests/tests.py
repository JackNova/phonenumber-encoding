import unittest
from number_encoding import PhoneNumberEncoder
from utils import create_mapping_dict, template

sample_dictionary = """an
                    blau
                    Bo"
                    Boot
                    bo"s
                    da
                    Fee
                    fern
                    Fest
                    fort
                    je
                    jemand
                    mir
                    Mix
                    Mixer
                    Name
                    neu
                    o"d
                    Ort
                    so
                    Tor
                    Torf
                    Wasser""".splitlines()

sample_phones = """112
                5624-82
                4824
                0721/608-4067
                10/783--5
                1078-913-5
                381482
                04824""".splitlines()

correct_output = """5624-82: mir Tor
                5624-82: Mix Tor
                4824: Torf
                4824: fort
                4824: Tor 4
                10/783--5: neu o"d 5
                10/783--5: je bo"s 5
                10/783--5: je Bo" da
                381482: so 1 Tor
                04824: 0 Torf
                04824: 0 fort
                04824: 0 Tor 4""".splitlines()

class TestNumberEncodings(unittest.TestCase):

    def test_correct_encoding_on_sample_data(self):
        expected_results = [s.strip() for s in correct_output]
        mapping_dict = create_mapping_dict("E | J N Q | R W X | D S Y | F T | A M | C I V | B K U | L O P | G H Z")
        words_list = sample_dictionary

        phone_number_encoder = PhoneNumberEncoder(mapping_dict=mapping_dict, words_list=words_list)

        for phone_number in sample_phones:
            encodings = phone_number_encoder.get_encodings(phone_number, separator=" ")
            for encoding in encodings:
                expected_output = template(phone_number, encoding)
                assert expected_output in expected_results
                expected_results.remove(expected_output)
            
            assert len(expected_results) == 0


if __name__ == '__main__':
    unittest.main()