import unittest
from mocks import sample_dictionary
from indexing_strategies.lookup_by_encoding import Index
from utils import create_mapping_dict
import sys
import logging
import main as m

my_word = 'EJRDFACBLG'
strange_word = 'EJRD-FAC"BLG'

class TestMain(unittest.TestCase):

    def test_capture_stdout(self):
        words_list = ['ciao']
        source_stream = iter(['6658'])
        m.run(words_list=words_list, source_stream=source_stream)
        assert sys.stdout.getvalue().strip() == "6658: ciao"

    def test_nothing_is_printed_when_no_possible_encoding(self):
        words_list = ['xxxxxxxx']
        source_stream = iter(['6658'])
        m.run(words_list=words_list, source_stream=source_stream)
        assert sys.stdout.getvalue().strip() == ""


if __name__ == '__main__':
    unittest.main()