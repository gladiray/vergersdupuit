# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-06 09:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0004_auto_20170411_0504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('season', models.CharField(blank=True, max_length=200, null=True, verbose_name='Season')),
                ('photo', models.ImageField(upload_to='upload/', verbose_name='Products photo')),
            ],
        ),
        migrations.CreateModel(
            name='ProductsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
            },
            bases=('pages.page', models.Model),
        ),
        migrations.AddField(
            model_name='product',
            name='container_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.ProductsPage'),
        ),
    ]