import os
import re

from furnace.services.service_base import ServiceBase
from furnace.models.fixture_item_model import FixtureItemModel
from furnace.models.fixture_page_model import FixturePageModel
from furnace.globals.const import const


class FixtureLocatorService(ServiceBase):
    def __init__(self, *args, **kwargs):
        super(ServiceBase, self).__init__(*args, **kwargs)

        self._fixture_root = os.path.normpath(os.path.join(os.path.split(__file__)[0], r'../fixtures'))

    @property
    def root(self):
        return self._fixture_root

    def get_fixtures_entries(self):
        """
        return a dict contain the content information of the fixture directory
        """
        fixture_indexes = []
        for root, dirs, files in os.walk(self._fixture_root):
            root_path, parent_folder = os.path.split(root)
            relative_root = root.replace(self._fixture_root, '')
            if relative_root:
                if relative_root[0] == '\\' or relative_root[0] == '/':
                    relative_root = 'fixtures/' + relative_root[1:]
                else:
                    relative_root = 'fixtures/' + relative_root[0]
            else:
                relative_root = 'fixtures'
            fim = FixtureItemModel()
            fixture_indexes.append(fim)
            fim.relative_path_to_root = relative_root
            fim.parent_folder_name = parent_folder
            other_pages = []
            for file in files:
                file = file.lower()
                if file == const.index_page:
                    fim.is_found_index = True
                    fim.index_path = os.path.join(relative_root, const.index_page)

                elif file.endswith('.tpl.html'):
                    # TODO handling in future
                    pass

                elif file.endswith('.html'):
                    pm = FixturePageModel()
                    pm.relative_path = os.path.join(relative_root, file)
                    # TODO: Move the convert logic to filter split_and_upper_first_letter.py
                    pm.name = ' '.join(re.split(r'[^a-zA-Z]+', os.path.splitext(file)[0]))
                    pm.name = pm.name[0].upper() + pm.name[1:]
                    other_pages.append(pm)

            fim.other_pages = tuple(other_pages)
        return tuple(fixture_indexes)
