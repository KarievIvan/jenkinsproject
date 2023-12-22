import unittest
from Lab2 import DitsadokQueue
# -*- coding: utf-8 -*-
import sys
import codecs
sys.stdout = codecs.getwriter("iso-8859-1")(sys.stdout, 'xmlcharrefreplace')
class TestDitsadokQueue(unittest.TestCase):
    
    def setUp(self):
        self.ditsadok_queue = DitsadokQueue()

 

if __name__ == '__main__':
    unittest.main()

