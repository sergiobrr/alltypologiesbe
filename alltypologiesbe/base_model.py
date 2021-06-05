from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name='Creato il')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificato il')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.__class__.__name__}-{self.id}'
