'''
Tests for the functions from the 'key' module
'''
import he.key as hk
import random
import unittest


class nxtodd_test(unittest.TestCase):
    def test_nxtodd(self):
        '''
        Tests, must return next odd values:
        '''
        self.assertFalse(hk.nxtodd(1) == 2)
        self.assertTrue(hk.nxtodd(2) == 3)
        self.assertTrue(hk.nxtodd(123) == 123)
        self.assertTrue(hk.nxtodd(1000) == 1001)
        self.assertFalse(hk.nxtodd(2) == 2)


class complexroot_test(unittest.TestCase):
    def test_complexroot(self):
        '''
        Test, must return right pair of complex roots
        '''
        for i in range(10):
            brd = random.randint(15)
            (a,b) = hk.complexroot(10)
            self.assertTrue(a.real < brd)
            self.assertTrue(b.imag < brd)
            self.assertFalse(a.imag > brd)
            self.assertFalse(b.real == brd)


