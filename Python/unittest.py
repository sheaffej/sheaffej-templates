#!/usr/bin/env python
from __future__ import print_function
import unittest


class TestXXX(unittest.TestCase):

    def setUp(self):
        print()

    def tearDown(self):
        pass

    def test_dummy(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()

