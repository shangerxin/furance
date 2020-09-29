from django.db import models
from furnace.models.model_base import ModeBase


class ActionModel(ModeBase):
    action_type = models.IntegerField(default=0)
    action_start = models.DateTimeField()
    action_end = models.DateTimeField()
    action_target = models.CharField(max_length=128)
    action_description = models.CharField(max_length=256)

    def __str__(self):
        return super().__str__()


