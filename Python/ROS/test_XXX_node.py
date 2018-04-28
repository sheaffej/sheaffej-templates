#!/usr/bin/env python
from __future__ import print_function
import threading
import unittest

import rospy

PKG = 'XXX'
NAME = 'XXX_node_test'


class TestXXXNode(unittest.TestCase):

    def __init__(self, *args):
        super(TestXXXNode, self).__init__(*args)

        self.lock = threading.RLock()

        rospy.init_node("XXX_test", log_level=rospy.DEBUG)
        rospy.Subscriber("/XXX/XXX", XXX_msg, self._XXX_callback)
        self.pub_XXX = rospy.Publisher(
            '/XXX/XXX', XXX_msg, queue_size=1
        )
        rospy.sleep(1)  # Let subscribers connect

    def test_dummy(self):
        self.assertTrue(True)


if __name__ == '__main__':
    import rostest
    rostest.rosrun(PKG, NAME, TestXXXNode)
