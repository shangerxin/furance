from django.db import models


class ModeBase(models.Model):
    object_manager = models.Manager()

    def __init__(self, *args, **kwargs):
        super(ModeBase, self).__init__(*args, **kwargs)
        self.id = models.AutoField(primary_key=True)

    class Meta(object):
        abstract = True
        app_label = 'furnace'



