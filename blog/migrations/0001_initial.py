# Generated by Django 3.0.8 on 2020-07-28 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_site_name', models.CharField(max_length=200)),
                ('current_main_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('current_categorie', models.CharField(blank=True, max_length=200)),
                ('current_details', models.TextField(blank=True)),
                ('current_details_2', models.TextField(blank=True)),
                ('current_design_photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('current_design_photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('current_design_photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('current_thoughts', models.TextField(blank=True)),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('show', models.BooleanField(default=True)),
                ('current_project_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('project_main_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('categorie', models.CharField(max_length=200)),
                ('details_main', models.TextField(blank=True)),
                ('detail_2', models.TextField(blank=True)),
                ('product_design', models.TextField(blank=True)),
                ('product_design_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('design_photo2', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('design_detail_1', models.TextField(blank=True)),
                ('design_detail_2', models.TextField(blank=True)),
                ('design_detail_3', models.TextField(blank=True)),
                ('design_detail_4', models.TextField(blank=True)),
                ('final_photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('final_photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('final_photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('final_photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('final_photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('final_photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('final_photo_7', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('final_photo_8', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('show', models.BooleanField(default=True)),
                ('project_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
