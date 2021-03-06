# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-04 09:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20190604_0917'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('text', mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Text content')),
                ('text_fr', mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Text content')),
                ('text_en', mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Text content')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='upload/', verbose_name='Photo 1')),
                ('alt_photo1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Alternative text for photo1')),
                ('alt_photo1_fr', models.CharField(blank=True, max_length=200, null=True, verbose_name='Alternative text for photo1')),
                ('alt_photo1_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Alternative text for photo1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='upload/', verbose_name='Photo 2')),
                ('alt_photo2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Alternative text for photo2')),
                ('alt_photo2_fr', models.CharField(blank=True, max_length=200, null=True, verbose_name='Alternative text for photo2')),
                ('alt_photo2_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Alternative text for photo2')),
                ('extra_css_for_section', models.CharField(blank=True, help_text='{background-color: #9D090E;color: white;}', max_length=2000, null=True, verbose_name='CSS to add to section')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.HomePage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
