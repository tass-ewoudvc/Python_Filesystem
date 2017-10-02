#!/usr/bin/env python

"""
<Copyright ?>
"""

import unittest


def dict_inverse(in_dict):
    """ "inverses" a dictionary
    Uses values as keys for the new dict.
    The old keys end up in a list if they had equal values.
    Follows the rules of dictionaries, no mutable types as keys.
    So the passed list cannot have mutable types as values.
    """
    new_dict = {}
    for k, value in in_dict.items():
        if value not in new_dict:
            new_dict[value] = [k]
        else:
            new_dict[value].append(k)
    return new_dict


def dict_inverse3(in_dict):
    new_dict = {}
    for k,v in in_dict.items():
        l = new_dict.get(v, [])
        l.append(k)
        new_dict[v] = l
    return new_dict


def dict_inverse2(in_dict):
    new_dict = {}
    for k in in_dict:
        if in_dict[k] not in new_dict:
            new_dict[in_dict[k]] = [k]
        else:
            new_dict[in_dict[k]].append(k)
    return new_dict


def dict_inverse4(in_dict):
    new_dict = {}
    for k, value in in_dict.items():
        if value not in new_dict:
            new_dict[value] = []
        new_dict[value].append(k)
    return new_dict


class TestDictInverse(unittest.TestCase):
    """
    Test class for dict_inverse
    """
    def test_dict_inverse(self):
        """ Tests the dict_inverse function """
        codes = {"Oostende": 8400,
                 "Zandvoorde": 8400,
                 "Stene": 8400,
                 "Brugge": 8000,
                 "Gent": 9000
                 }

        inversed = dict_inverse4(codes)

        self.assertEqual(len(inversed), 3)

        self.assertEqual(len(inversed[8400]), 3)
        for city in ("Oostende", "Zandvoorde", "Stene"):
            self.assertTrue(city in inversed[8400])

        self.assertEqual(inversed[8000], ["Brugge"])
        self.assertEqual(inversed[9000], ["Gent"])

if __name__ == "__main__":
    unittest.main()
