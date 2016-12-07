# -*- coding: utf-8 -*-

import unittest

from pysnippets import dictsnippets as dsnippets
from pysnippets import listsnippets as lsnippets


class DictSnippetsTest(unittest.TestCase):
    def testFilter(self):
        self.assertEqual(dsnippets.filter({'a': 1, 'b': 2, 'c': 3}, ['c', 'd:4']), {'c': 3, 'd': 4})
        self.assertEqual(dsnippets.filter({'a': 1, 'b': 2, 'c': 3}, ['c', 'd:4'], exec_eval=False), {'c': 3, 'd': '4'})

    def testGets(self):
        self.assertEqual(dsnippets.gets({'a': 1, 'b': 2, 'c': 3}, ['c', 'd:4']), [3, 4])
        self.assertEqual(dsnippets.gets({'a': 1, 'b': 2, 'c': 3}, ['c', 'd:4'], exec_eval=False), [3, '4'])


class ListSnippetsTest(unittest.TestCase):
    def setUp(self):
        self.list_ = [1, 2, 3]

    def testAll(self):
        # Tuple
        self.assertTrue(lsnippets.all(self.list_, (1, 2)))
        self.assertFalse(lsnippets.all(self.list_, (1, 5)))
        self.assertFalse(lsnippets.all(self.list_, (4, 5)))
        # List
        self.assertTrue(lsnippets.all(self.list_, [1, 2]))
        self.assertFalse(lsnippets.all(self.list_, [1, 5]))
        self.assertFalse(lsnippets.all(self.list_, [4, 5]))

    def testAny(self):
        # Tuple
        self.assertTrue(lsnippets.any(self.list_, (1, 2)))
        self.assertTrue(lsnippets.any(self.list_, (1, 5)))
        self.assertFalse(lsnippets.any(self.list_, (4, 5)))
        # List
        self.assertTrue(lsnippets.any(self.list_, [1, 2]))
        self.assertTrue(lsnippets.any(self.list_, [1, 5]))
        self.assertFalse(lsnippets.any(self.list_, [4, 5]))


if __name__ == '__main__':
    unittest.main()
