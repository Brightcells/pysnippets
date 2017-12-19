# -*- coding: utf-8 -*-

import re

from .compat import basestring


class StrSnippets(object):
    def strip_ascii_control_characters(self, s):
        # ASCII Control Characters
        return re.sub(r'[\x01-\x1F\x7F]', '', s)

    def strip(self, s, cc=False):
        if not isinstance(s, basestring):
            return s
        return self.strip_ascii_control_characters(s) if cc else s.strip()


_global_instance = StrSnippets()
strip = _global_instance.strip
