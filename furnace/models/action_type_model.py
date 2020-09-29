from furnace.models.model_base import ModeBase
from django.db import models


class ActionTypeModel(ModeBase):
    id = models.IntegerField()
    type = models.CharField(max_length=64)
