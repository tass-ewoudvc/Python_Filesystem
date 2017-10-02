#!/usr/bin/env python

"""
Tass PythonFundamentals Course
Solution to: "Palindrome Tester"
"""

import unittest

def is_palindrome(string):
    """ Tests if string is a palindrome """
    # Cheating ... Using the extended slice syntax
    # You could also just use reversed
    return string[::-1] == string


class TestPalindrome(unittest.TestCase):
    """
    Test class for is_palindrome
    """
    def test_is_palindrome(self):
        """ Tests the is_palindrome function """
        for string in ("abba",
                       "satanoscillatemymetallicsonatas",
                       "kayak",
                       "boob"
                       ):
            self.assertTrue(is_palindrome(string))

        self.assertFalse(is_palindrome("boek"))

unittest.main()
