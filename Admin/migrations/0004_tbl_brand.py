# Generated by Django 5.1.3 on 2024-12-05 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_adminreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
            ],
        ),
    ]
