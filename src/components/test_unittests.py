import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

import unittest
from unittest.mock import patch, mock_open
import json
import dataStorage
import itemClass

class TestDataStorage(unittest.TestCase):
    @patch('tkinter.filedialog.askopenfile', return_value=None)
    def test_load_no_file_selected(self, mock_askopenfile):
        self.assertEqual(dataStorage.load(), None)

    @patch('tkinter.filedialog.askopenfile')
    def test_load_valid_file(self, mock_askopenfile):
        # Mocking the file content
        file_content = '[{"job": "Test Job", "date": "2023-04-01", "description": "Test Description", "amount": 100}]'

        # Setup mock to return a mock file object that returns the file_content string when read is called
        mock_file = mock_open(read_data=file_content)
        mock_askopenfile.return_value = mock_file()

        # Expected result
        expected = [itemClass.Entry("Test Job", "2023-04-01", "Test Description", 100)]

        # Convert expected result to dicts for comparison since we can't directly compare objects
        result = dataStorage.load()
        result_dicts = [item.to_dict() for item in result]
        expected_dicts = [item.to_dict() for item in expected]

        self.assertEqual(result_dicts, expected_dicts)

    @patch('builtins.open', new_callable=mock_open)
    def test_save(self, mock_file):
        # Setup your test data and expected result
        test_data = [itemClass.Entry("Test Job", "2023-04-01", "Test Description", 100)]
        expected_json = '[{"job": "Test Job", "date": "2023-04-01", "description": "Test Description", "amount": 100}]'
        
        # Call the method under test
        dataStorage.save(test_data)
        
        # Capture all arguments to write calls
        write_calls = mock_file().write.call_args_list
        written_content = ''.join(call_arg[0][0] for call_arg in write_calls)
        
        # Parse both strings to JSON objects for comparison
        expected_data = json.loads(expected_json)
        written_data = json.loads(written_content)
        
        # Assert the parsed JSON objects are equal
        self.assertEqual(written_data, expected_data)

if __name__ == '__main__':
    unittest.main()