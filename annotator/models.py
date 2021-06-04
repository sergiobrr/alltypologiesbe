from django.db import models
from alltypologiesbe.base_model import BaseModel as Model

# Create your models here.


class Project(Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    randomize_document_order = models.BooleanField(default=False)

    class Meta:
        app_label = 'annotator'
        verbose_name = 'Progetto'
        verbose_name_plural = 'Progetti'
        ordering = ['name', '-created_at']
