# -*- coding: utf-8 -*-

from pysnippets import dictsnippets as dsn


class TestPyDictSnippetsCommands(object):

    def test_filter(self):
        dict_ = {'a': 1, 'b': 2, 'c': 3}
        assert dsn.filter(dict_, ['c', 'd:4']) == {'c': 3, 'd': 4}
        assert dsn.filter(dict_, ['c', 'd:4'], exec_eval=False) == {'c': 3, 'd': '4'}

    def test_gets(self):
        dict_ = {'a': 1, 'b': 2, 'c': 3}
        assert dsn.gets(dict_, ['c', 'd:4']) == [3, 4]
        assert dsn.gets(dict_, ['c', 'd:4'], exec_eval=False) == [3, '4']
