from datetime import date
from nose.tools import eq_, ok_
try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch, MagicMock

from django.test import TestCase

from bpz.management.commands.load_cases import (parse_datetime,
                                                parse_raw_value)


class ParseTestCase(TestCase):

    def test_parse_datetime(self):
        value = "July 8, 2014"
        expected = date(2014, 7, 8)
        eq_(expected, parse_datetime(value))

    def test_parse_raw_value_plain(self):
        value = "City Council Chambers"
        expected = "City Council Chambers"
        eq_(expected, parse_raw_value(value))

    @patch("bpz.management.commands.load_cases.stderr")
    def test_parse_raw_value_with_newlines(self, stderr):
        stderr.write = MagicMock()
        value = "City Council Chambers\r\n\r\nCouncil Chambers"
        expected = "City Council Chambers"
        eq_(expected, parse_raw_value(value))
        ok_(stderr.write.called)
