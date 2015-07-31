import unittest
from mocks import sample_dictionary
from indexing_strategies.lookup_by_encoding import Index
from utils import create_mapping_dict

my_word = 'EJRDFACBLG'
strange_word = 'EJRD-FAC"BLG'

class TestLookupByEncoding(unittest.TestCase):

    def setUp(self):
        mapping_dict = create_mapping_dict("E | J N Q | R W X | D S Y | F T | A M | C I V | B K U | L O P | G H Z")
        self.index = Index(mapping_dict=mapping_dict, words_list=sample_dictionary)

    def test_encode_word(self):
        assert self.index.encode_word(my_word) == '0123456789'

    def test_ignores_capitalization(self):
        results_upper = self.index.encode_word(my_word.upper())
        results_lower = self.index.encode_word(my_word.lower())
        assert set(results_lower) == set(results_upper)

    def test_encode_word_with_dashes_and_quotes(self):
        assert self.index.encode_word(strange_word) == self.index.encode_word(strange_word.translate(None, '-"'))

    def test_lookup_index(self):
        assert self.index.lookup('4824') == ['fort', 'Torf']

if __name__ == '__main__':
    unittest.main()