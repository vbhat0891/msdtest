# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-30 19:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eBedTrack', '0002_auto_20170929_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('admin_id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_type', models.CharField(default=False, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('phone_no', models.CharField(max_length=12)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hadmin', to='eBedTrack.Administrator')),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=250)),
                ('phone_no', models.CharField(max_length=12)),
                ('admin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admnurses', to='eBedTrack.Administrator')),
                ('hospital_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosnurses', to='eBedTrack.Hospital')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('sex', models.CharField(max_length=10)),
                ('time_of_admission', models.DateTimeField(default=django.utils.timezone.now)),
                ('condition', models.CharField(max_length=30)),
                ('bed_type', models.CharField(max_length=10)),
                ('mode_of_arrival', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('injuries', models.CharField(blank=True, max_length=50)),
                ('deposition', models.CharField(blank=True, max_length=50)),
                ('time_of_surgery', models.CharField(blank=True, max_length=20)),
                ('kin_name', models.CharField(blank=True, max_length=50)),
                ('relation', models.CharField(blank=True, max_length=50)),
                ('time_of_death', models.CharField(blank=True, max_length=20)),
                ('updated_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('bed_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bedpatients', to='eBedTrack.Bed')),
                ('nurse_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nurpatients', to='eBedTrack.Nurse')),
            ],
        ),
        migrations.DeleteModel(
            name='Pateint',
        ),
        migrations.AddField(
            model_name='bed',
            name='hospital_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hosbeds', to='eBedTrack.Hospital'),
        ),
    ]
