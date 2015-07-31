import unittest
from number_encoding import PhoneNumberEncoder
from utils import create_mapping_dict, template
from mocks import sample_dictionary, sample_phones, correct_output
import logging

TOP_LONGEST_ENCODABLE_NUMBERS = ['352340887193903692613697064',
 '360134806347193903088369544',
 '014266787193903692613697064',
 '48769486193372699519385902',
 '473375885063402369544338608',
 '785571675468133692602697064',
 '806694549804676025134584719',
 '369206755369610190369260701',
 '340702961402960971937251690',
 '427880134546816027193783401',
 '7702727677193461519602719',
 '770272767719327679598719',
 '77023692055719375453428890',
 '6029283302719358986697064',
 '259236906186697064320691719',
 '208490371390643829516354681',
 '9598719376851977023697330',
 '587898860242598669706434034',
 '5270643703695447193553315950',
 '7713039037139064356163402675',
 '306630138077854681390369544',
 '362074602366902719360242590',
 '903088369544340702027852719',
 '8857367686454377028274719',
 '4278801345468160271936024259',
 '716602358369257701369873308',
 '602588905061027193459697064',
 '2544013468834513360295138719',
 '252505733091719378044696014',
 '289845469706436025134584719',
 '97355501909826970643904798',
 '58806160242047193517020694694',
 '77130385132624369544356163402',
 '0807428613458854681390369544',
 '01426678719378340170406869719',
 '9036926136970643703692517719',
 '36925190236954437140272069719',
 '26243695443614825546813360134',
 '771303602406369719356163402675',
 '407694697064371058461386697064',
 '407026023669027193903088369544',
 '9095730870248569017095138719',
 '259236906186697064349082046369',
 '903692613697064377023692064719',
 '7251701957345909083602366902719',
 '52706438830160236690271937064259',
 '2624369544382747193903088369544',
 '30873460226278669719358986697064',
 '527064388301602366902719370642590',
 '771303573768371934823027193903049']

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
            assert len(result) >=1
            assert all([len(phone_number) == len(coded.translate(None, '"- ')) for coded in result])

if __name__ == '__main__':
    unittest.main()