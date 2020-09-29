from furnace.models.model_base import ModeBase
from django.db import models


class FixtureItemModel(ModeBase):
    def __init__(self, *args, **kwargs):
        super(FixtureItemModel, self).__init__(self, *args, **kwargs)
        self.is_found_index = False
        self.other_pages = None
        self.parent_folder_name = None
        self.relative_path_to_root = None
        self.index_path = None
