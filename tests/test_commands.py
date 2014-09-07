from datetime import date
from nose.tools import eq_, ok_
try:
    from unittest.mock import patch, MagicMock
except ImportError:
    from mock import patch, MagicMock

from django.contrib.gis.gdal import DataSource
from django.test import TestCase

from bpz.management.commands.load_cases import (parse_datetime,
                                                parse_feature_raw_value)


class ParseTestCase(TestCase):

    def setUp(self):
        self.ds = DataSource('tests/fixtures/test-cases.json')

    def test_parse_datetime(self):
        value = "July 8, 2014"
        expected = date(2014, 7, 8)
        eq_(expected, parse_datetime(value))

    def test_parse_raw_value_plain(self):
        feature = self.ds[0][0]  # plain feature
        expected = "City Council Chambers"
        eq_(expected, parse_feature_raw_value(feature, 'Location'))

    @patch("bpz.management.commands.load_cases.stderr")
    def test_parse_raw_value_with_newlines(self, stderr):
        stderr.write = MagicMock()
        feature = self.ds[0][1]  # newlines feature
        expected = "City Council Chambers"
        eq_(expected, parse_feature_raw_value(feature, 'Location'))
        ok_(stderr.write.called)
