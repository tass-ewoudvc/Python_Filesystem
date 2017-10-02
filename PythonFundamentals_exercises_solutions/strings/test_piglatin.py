#!/usr/bin/env python

"""
Tass PythonFundamentals Course
Solution to: "Piglatin"
"""

import unittest
import piglatin

class TestPiglatin(unittest.TestCase):
    """
    Test class for Piglatin
    """
    def test_to_piglatin(self):
        """ Tests the to_piglatin function """
        self.assertEqual("appyhay", piglatin.to_piglatin("happy"))
        self.assertEqual("uckday", piglatin.to_piglatin("duck"))
        self.assertEqual("oveglay", piglatin.to_piglatin("glove"))
        self.assertEqual("eggway", piglatin.to_piglatin("egg"))
        self.assertEqual("inboxway", piglatin.to_piglatin("inbox"))

        self.assertEqual("appy-hay", piglatin.to_piglatin("happy", True))
        self.assertEqual("uck-day", piglatin.to_piglatin("duck", True))
        self.assertEqual("ove-glay", piglatin.to_piglatin("glove", True))
        self.assertEqual("egg-way", piglatin.to_piglatin("egg", True))
        self.assertEqual("inbox-way", piglatin.to_piglatin("inbox", True))


    def test_from_piglatin(self):
        """ Tests the from_piglatin function """
        self.assertEqual("happy", piglatin.from_piglatin("appy-hay"))
        self.assertEqual("duck", piglatin.from_piglatin("uck-day"))
        self.assertEqual("glove", piglatin.from_piglatin("ove-glay"))
        self.assertEqual("egg", piglatin.from_piglatin("egg-way"))
        self.assertEqual("inbox", piglatin.from_piglatin("inbox-way"))


unittest.main()
