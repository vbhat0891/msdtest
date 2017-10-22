# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-02 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eBedTrack', '0004_auto_20171002_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='bed_type',
            field=models.CharField(choices=[('AD ICU/CC', 'AD ICU/CC'), ('ER', 'ER'), ('MED/SURG', 'MED/SURG'), ('OB', 'OB'), ('SICU', 'SICU'), ('Neg Pres/Iso', 'Neg Pres/Iso'), ('OR', 'OR'), ('Peds', 'Peds'), ('PICU', 'PICU'), ('NICU', 'NICU'), ('Burn', 'Burn'), ('Mental_Health', 'Mental_Health'), ('Other', 'Other')], max_length=50),
        ),
    ]
