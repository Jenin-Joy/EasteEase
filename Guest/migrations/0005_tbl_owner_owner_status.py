# Generated by Django 5.1.3 on 2025-01-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_owner',
            name='owner_status',
            field=models.IntegerField(default=0),
        ),
    ]
