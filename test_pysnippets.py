# -*- coding: utf-8 -*-

"""
Copyright (c) 2016 HQM <qiminis0801@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

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
