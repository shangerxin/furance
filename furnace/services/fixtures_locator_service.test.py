import os
from django.test import TestCase

from furnace.services.fixtures_locator_service import FixtureLocatorService


class TestFixtureLocatorService(TestCase):

    def setUp(self):
        super().setUp()

        self.fls = FixtureLocatorService()

    def test_get_fixtures_index_pages(self):
        fixture_entries = self.fls.get_fixtures_entries()

