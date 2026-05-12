# test_bitmartapi.py
"""
Tests for BitMartAPI module.
"""

import unittest
from bitmartapi import BitMartAPI

class TestBitMartAPI(unittest.TestCase):
    """Test cases for BitMartAPI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BitMartAPI()
        self.assertIsInstance(instance, BitMartAPI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BitMartAPI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
