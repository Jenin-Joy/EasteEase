# Generated by Django 5.1.3 on 2025-01-30 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_tbl_place'),
        ('Owner', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_sellproperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sellproperty_details', models.CharField(max_length=50)),
                ('sellproperty_price', models.CharField(max_length=50)),
                ('sellproperty_photo', models.FileField(upload_to='Assets/owner/photo')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_category')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
            ],
        ),
    ]
