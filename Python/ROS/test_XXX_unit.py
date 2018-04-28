#!/usr/bin/env python
from __future__ import print_function
import unittest


PKG = 'XXX'
NAME = 'XXX_unittest'


class TestXXX(unittest.TestCase):

    def __init__(self, *args):
        super(TestXXX, self).__init__(*args)

    def test_dummy(self):
        # (x, y, expected)
        tests = [
            (1, 1, 1)
        ]

        print()
        for x, y, expected in tests:
            actual = 1
            print("Actual: {}, Expected: {}".format(actual, expected))
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    import rosunit
    rosunit.unitrun(PKG, NAME, TestXXX)
