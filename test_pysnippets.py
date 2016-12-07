# -*- coding: utf-8 -*-

import unittest

import pysnippets.dictsnippets as dsnippets


class DictSnippetsTest(unittest.TestCase):
    def testFilter(self):
        self.assertEqual(dsnippets.filter({'a': 1, 'b': 2, 'c': 3}, ['c', 'd:4']), {'c': 3, 'd': 4})
        self.assertEqual(dsnippets.filter({'a': 1, 'b': 2, 'c': 3}, ['c', 'd:4'], exec_eval=False), {'c': 3, 'd': '4'})

    def testGets(self):
        self.assertEqual(dsnippets.gets({'a': 1, 'b': 2, 'c': 3}, ['c', 'd:4']), [3, 4])
        self.assertEqual(dsnippets.gets({'a': 1, 'b': 2, 'c': 3}, ['c', 'd:4'], exec_eval=False), [3, '4'])


if __name__ == '__main__':
    unittest.main()
