# -*- coding: utf-8 -*-

from pysnippets import strsnippets as ssn


class TestPyStrSnippetsCommands(object):

    def test_strip(self):
        assert ssn.strip(None) is None
        assert ssn.strip({'a': 1}) == {'a': 1}
        assert ssn.strip(' xyz ') == 'xyz'
