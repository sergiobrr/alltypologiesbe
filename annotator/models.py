from django.db import models
from alltypologiesbe.base_model import BaseModel as Model
from django.db.models import Index
from django.urls import reverse
from django.contrib.postgres import indexes, search


class Project(Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default='')
    randomize_document_order = models.BooleanField(default=False)

    class Meta:
        app_label = 'annotator'
        verbose_name = 'Progetto'
        verbose_name_plural = 'Progetti'
        ordering = ['name', '-created_at']

    def get_absolute_url(self):
        return reverse('api_v1:project-detail', args=[self.id, ])


offers_search_vector = search.SearchVector('text', config='italian')


class Offer(Model):
    text = models.TextField()
    project = models.ForeignKey(Project, related_name='documents', on_delete=models.CASCADE)
    meta = models.TextField(default='{}')

    class Meta:
        app_label = 'annotator'
        verbose_name = 'Offerta'
        verbose_name_plural = 'Offerte'
        indexes = [
            indexes.GinIndex(offers_search_vector, name='idx_offer_text_fullsearch'),
            Index(fields=['text', ], name='idx_offer_text')
        ]
