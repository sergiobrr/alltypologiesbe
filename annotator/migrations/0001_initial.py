# Generated by Django 3.2.4 on 2021-06-04 10:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Creato il')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Modificato il')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('randomize_document_order', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Progetto',
                'verbose_name_plural': 'Progetti',
                'ordering': ['name', '-created_at'],
            },
        ),
    ]