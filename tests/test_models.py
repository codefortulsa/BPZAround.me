#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_models
----------------------------------

Tests for bpz models
"""

from django.test import TestCase

from bpz.models import Case, HomeOwnersAssociation


class CaseTestCase(TestCase):

    def test_str(self):
        case = Case(case_id='BOA-21745')
        self.assertEqual(str(case), 'BOA-21745')


class HomeOwnersAssociationTestCase(TestCase):

    def test_str(self):
        hoa = HomeOwnersAssociation()
        self.assertEqual(str(hoa), '<unnamed>')
        hoa.name = 'Home Owners United'
        self.assertEqual(str(hoa), 'Home Owners United')
