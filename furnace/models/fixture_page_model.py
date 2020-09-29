from furnace.models.model_base import ModeBase
from django.db import models


class FixturePageModel(ModeBase):
    def __init__(self, *args, **kwargs):
        super(FixturePageModel, self).__init__(self, *args, **kwargs)
        self.name = None
        self.relative_path = None
