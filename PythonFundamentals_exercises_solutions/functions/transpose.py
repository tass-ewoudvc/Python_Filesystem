#!/usr/bin/env python

"""
Tass PythonFundamentals Course
Solution to: "Matrix transposition"
"""

import unittest

def transpose(matrix):
    """ Transposes a given matrix """
    # return tuple( tuple([row[i] for row in matrix])
    #               for i in range(len(matrix[0])))
    return tuple(tuple(row[i] for row in matrix) for i in range(len(matrix[0])))

class TestTranspose(unittest.TestCase):
    """
    Test class for Matrix Transposition
    """
    def test_transpose(self):
        """ Tests the transpose function """
        matrix = ((1, 2), (3, 4), (5, 6))
        matrix_t = ((1, 3, 5), (2, 4, 6))
        self.assertEqual(matrix_t, transpose(matrix))

        matrix = ((1,),)
        self.assertEqual(matrix, transpose(matrix))

        matrix = ((1, 2), (3, 4))
        matrix_t = ((1, 3), (2, 4))
        self.assertEqual(matrix_t, transpose(matrix))
        

unittest.main()
