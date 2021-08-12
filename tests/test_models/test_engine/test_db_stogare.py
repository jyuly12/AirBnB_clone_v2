#!/usr/bin/python3
"""Test bd_storage"""

from unittest import TestCase
import unittest
import os

@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "No apply for db")
class test_DBStorage(TestCase):
    """test database"""
    def test_db(self):
        """ pass"""
        pass

if __name__ == "__main__":
    unittest.main()