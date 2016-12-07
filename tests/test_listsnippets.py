# -*- coding: utf-8 -*-

from pysnippets import listsnippets as lsn


class TestPyDictSnippetsCommands(object):

    def test_all(self):
        list_ = [1, 2, 3]
        assert lsn.all(list_, (1, 2))
        assert not lsn.all(list_, [1, 5])
        assert not lsn.all(list_, [4, 5])

    def test_any(self):
        list_ = [1, 2, 3]
        assert lsn.any(list_, (1, 2))
        assert lsn.any(list_, [1, 5])
        assert not lsn.any(list_, [4, 5])
