# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-03-03 16:26


import django.utils.timezone
import model_utils.fields
import simple_history.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('experiments', '0003_auto_20170713_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalExperimentKeyValue',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('experiment_id', models.PositiveSmallIntegerField(db_index=True, verbose_name='Experiment ID')),
                ('key', models.CharField(max_length=255)),
                ('value', models.TextField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Experiment Key-Value Pair',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
