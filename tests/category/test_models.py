#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-knowledgebase
------------

Tests for `django-knowledgebase` models module.
"""

from __future__ import absolute_import, unicode_literals

from support_tickets.models import Category
from ..tests import TicketCategorySetUpMixin


class CategoryTest(TicketCategorySetUpMixin):

    def test_create_new_category(self):
        obj1 = self.categories[2]
        obj2 = self.tickets_one[0]

        self.assertTrue(obj1.title)
        self.assertTrue(obj1.created)
        self.assertTrue(obj1.modified)

        self.assertEqual(obj1.title, str(obj1))
        self.assertEqual(obj1.title, 'Category3')
        self.assertEqual(obj2.author, self.user_one)

    def test_category_querysets(self):
        self.assertEqual(len(Category.objects.by_author(self.user_one)), 3)
        self.assertEqual(len(Category.objects.by_author(self.user_two)), 5)

    def tearDown(self):
        pass
