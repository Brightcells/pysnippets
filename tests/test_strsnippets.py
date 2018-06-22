# -*- coding: utf-8 -*-

from pysnippets import strsnippets as ssn


class TestPyStrSnippetsCommands(object):

    def test_strip(self):
        assert ssn.strip(None) is None
        assert ssn.strip({'a': 1}) == {'a': 1}
        assert ssn.strip(' xyz ') == 'xyz'

    # def test_strip_cc(self):
    #     # ASCII vs. Unicode
    #     assert ssn.strip(u'\u202d18888888888\u202c', cc=True) == u'18888888888'

    def test_trim(self):
        assert ssn.trim(None) is None
        assert ssn.trim({'a': 1}) == {'a': 1}
        assert ssn.trim('qwertyuiop', 3) == 'qwe'
        assert ssn.trim('qwertyuiop', 3, '...') == 'qwe...'

    def test_removeU2006(self):
        assert ssn.removeU2006('iOS\xe2\x80\x86') == 'iOS'
        assert ssn.removeU2006(u'iOS\u2006') == 'iOS'
