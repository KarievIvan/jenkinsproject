import unittest
from Lab2 import DitsadokQueue
# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')class TestDitsadokQueue(unittest.TestCase):
    
    def setUp(self):
        self.ditsadok_queue = DitsadokQueue()

    def test_add_child_to_queue(self):
        self.ditsadok_queue.add_child_to_queue("Дитина1")
        self.assertEqual(self.ditsadok_queue.queue, ["Дитина1"])

        self.ditsadok_queue.add_child_to_queue("Дитина2")
        self.assertEqual(self.ditsadok_queue.queue, ["Дитина1", "Дитина2"])

    def test_remove_child_from_queue(self):
        self.ditsadok_queue.remove_child_from_queue()
        self.assertEqual(self.ditsadok_queue.queue, [])

        self.ditsadok_queue.add_child_to_queue("Дитина1")
        self.ditsadok_queue.add_child_to_queue("Дитина2")
        self.ditsadok_queue.remove_child_from_queue()
        self.assertEqual(self.ditsadok_queue.queue, ["Дитина2"])

    def test_display_queue(self):
        self.ditsadok_queue.display_queue()
        self.assertEqual(self.ditsadok_queue.queue, [])

        self.ditsadok_queue.add_child_to_queue("Дитина1")
        self.ditsadok_queue.add_child_to_queue("Дитина2")
        self.ditsadok_queue.display_queue()
        self.assertEqual(self.ditsadok_queue.queue, ["Дитина1", "Дитина2"])

if __name__ == '__main__':
    unittest.main()

