'''
Tests for the functions from the 'encryption' module
'''
import he.encrypt as hen
import random
import unittest




class inttopoly_test(unittest.TestCase):
    def test_inttopoly(self):
        '''
        Tests for inntopoly function:
        '''
        self.assertFalse(hen.nxtodd(1) == 2)
        self.assertTrue(hen.nxtodd(2) == 3)
        self.assertTrue(hen.nxtodd(123) == 123)
        self.assertTrue(hen.nxtodd(1000) == 1001)
        self.assertFalse(hen.nxtodd(2) == 2)

