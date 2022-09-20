from django.db import models

class BaseModelMixin(models.Model):
    date_added = models.DateField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True