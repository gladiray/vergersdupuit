# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-04 09:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20190604_0726'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('content_fr', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_en', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='StartPageSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('text', mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Text for section')),
                ('text_fr', mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Text for section')),
                ('text_en', mezzanine.core.fields.RichTextField(blank=True, null=True, verbose_name='Text for section')),
                ('photo1', models.ImageField(blank=True, null=True, upload_to='upload/', verbose_name='Photo 1')),
                ('alt_photo1', models.CharField(blank=True, help_text='Text to display when image is not available, this is important for serach engines and text readers', max_length=200, null=True, verbose_name='Alternative text for image 1')),
                ('alt_photo1_fr', models.CharField(blank=True, help_text='Text to display when image is not available, this is important for serach engines and text readers', max_length=200, null=True, verbose_name='Alternative text for image 1')),
                ('alt_photo1_en', models.CharField(blank=True, help_text='Text to display when image is not available, this is important for serach engines and text readers', max_length=200, null=True, verbose_name='Alternative text for image 1')),
                ('photo2', models.ImageField(blank=True, null=True, upload_to='upload/', verbose_name='Photo 1')),
                ('alt_photo2', models.CharField(blank=True, help_text='Text to display when image is not available, this is important for serach engines and text readers', max_length=200, null=True, verbose_name='Alternative text for image 2')),
                ('alt_photo2_fr', models.CharField(blank=True, help_text='Text to display when image is not available, this is important for serach engines and text readers', max_length=200, null=True, verbose_name='Alternative text for image 2')),
                ('alt_photo2_en', models.CharField(blank=True, help_text='Text to display when image is not available, this is important for serach engines and text readers', max_length=200, null=True, verbose_name='Alternative text for image 2')),
                ('extra_css_for_section', models.CharField(blank=True, help_text='for exemple:  {background-color: #9D090E;color: white;}', max_length=2000, null=True, verbose_name='extra CSS for section')),
                ('container_startpage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.StartPage')),
            ],
            options={
                'ordering': ('_order',),
            },
        ),
    ]
