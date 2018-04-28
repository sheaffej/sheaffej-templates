#!/usr/bin/env python3
from __future__ import print_function
import unittest


class TestXXX(unittest.TestCase):

    def __init__(self, *args):
        super(TestXXX, self).__init__(*args)

    def test_dummy(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()

