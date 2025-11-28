#!/usr/bin/env python3
"""
Test cases for read_write_heap.py script
"""

import unittest
import sys
import os
from unittest.mock import patch, mock_open, MagicMock


class TestUsageError(unittest.TestCase):
    """Test cases for usage_error function"""

    def test_usage_error_output(self):
        """Test that usage_error prints correct message and exits"""
        with self.assertRaises(SystemExit) as cm:
            with patch('sys.stdout') as mock_stdout:
                from read_write_heap import usage_error
                usage_error("Test error message")
        
        self.assertEqual(cm.exception.code, 1)


class TestMainFunction(unittest.TestCase):
    """Test cases for main function"""

    def test_wrong_number_of_arguments(self):
        """Test with wrong number of command line arguments"""
        test_cases = [
            [],
            ['script.py'],
            ['script.py', '123'],
            ['script.py', '123', 'search'],
            ['script.py', '123', 'search', 'replace', 'extra']
        ]
        
        for args in test_cases:
            with self.subTest(args=args):
                with patch('sys.argv', ['read_write_heap.py'] + args):
                    with self.assertRaises(SystemExit) as cm:
                        from read_write_heap import main
                        main()
                    self.assertEqual(cm.exception.code, 1)

    def test_invalid_pid(self):
        """Test with non-integer PID"""
        with patch('sys.argv', ['read_write_heap.py', 'not_a_number', 'search', 'replace']):
            with self.assertRaises(SystemExit) as cm:
                from read_write_heap import main
                main()
            self.assertEqual(cm.exception.code, 1)

    def test_non_ascii_strings(self):
        """Test with non-ASCII strings"""
        non_ascii_cases = [
            ('café', 'replace'),
            ('search', 'café'),
            ('🚀', 'test'),
            ('test', '🎯')
        ]
        
        for search, replace in non_ascii_cases:
            with self.subTest(search=search, replace=replace):
                with patch('sys.argv', ['read_write_heap.py', '123', search, replace]):
                    with self.assertRaises(SystemExit) as cm:
                        from read_write_heap import main
                        main()
                    self.assertEqual(cm.exception.code, 1)

    def test_replace_string_longer_than_search(self):
        """Test when replace string is longer than search string"""
        with patch('sys.argv', ['read_write_heap.py', '123', 'short', 'very_long_replace']):
            with self.assertRaises(SystemExit) as cm:
                from read_write_heap import main
                main()
            self.assertEqual(cm.exception.code, 1)


class TestReadWriteHeapFunction(unittest.TestCase):
    """Test cases for read_write_heap function"""

    @patch('builtins.open')
    @patch('os.path.exists')
    def test_heap_region_not_found(self, mock_exists, mock_open):
        """Test when heap region is not found in memory maps"""
        mock_exists.return_value = True
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.return_value = "no heap here"
        
        from read_write_heap import read_write_heap
        result = read_write_heap(1234, "test", "replace")
        self.assertFalse(result)

    @patch('builtins.open')
    @patch('os.path.exists')
    def test_string_not_found_in_heap(self, mock_exists, mock_open):
        """Test when search string is not found in heap"""
        mock_exists.return_value = True
        
        maps_content = "5555-6666 rw-p 00000000 00:00 0 [heap]"
        mock_file = mock_open.return_value.__enter__.return_value
        mock_file.read.side_effect = [maps_content, b"some random heap data"]
        
        from read_write_heap import read_write_heap
        result = read_write_heap(1234, "nonexistent", "replace")
        self.assertFalse(result)

    @patch('builtins.open')
    @patch('os.path.exists')
    def test_permission_error(self, mock_exists, mock_open):
        """Test handling of permission errors"""
        mock_exists.return_value = True
        mock_open.side_effect = PermissionError("Permission denied")
        
        from read_write_heap import read_write_heap
        result = read_write_heap(1234, "test", "replace")
        self.assertFalse(result)

    @patch('builtins.open')
    @patch('os.path.exists')
    def test_process_not_found(self, mock_exists, mock_open):
        """Test handling of non-existent process"""
        mock_exists.return_value = False
        
        from read_write_heap import read_write_heap
        result = read_write_heap(99999, "test", "replace")
        self.assertFalse(result)


class TestDocumentation(unittest.TestCase):
    """Test that all functions have proper documentation"""

    def test_module_docstring(self):
        """Test module has docstring"""
        import read_write_heap
        self.assertIsNotNone(read_write_heap.__doc__)
        self.assertGreater(len(read_write_heap.__doc__), 0)

    def test_function_docstrings(self):
        """Test all functions have docstrings"""
        from read_write_heap import usage_error, read_write_heap, main
        
        self.assertIsNotNone(usage_error.__doc__)
        self.assertIsNotNone(read_write_heap.__doc__)
        self.assertIsNotNone(main.__doc__)
        
        self.assertGreater(len(usage_error.__doc__), 0)
        self.assertGreater(len(read_write_heap.__doc__), 0)
        self.assertGreater(len(main.__doc__), 0)


if __name__ == '__main__':
    unittest.main()
