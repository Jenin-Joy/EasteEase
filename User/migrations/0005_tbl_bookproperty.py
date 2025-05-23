# Generated by Django 5.1.3 on 2025-02-27 05:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_tbl_owner_owner_status'),
        ('Owner', '0008_tbl_sellproperty'),
        ('User', '0004_alter_tbl_rentbooking_rentbooking_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_bookproperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookproperty_date', models.DateField(auto_now_add=True)),
                ('bookproperty_amount', models.CharField(max_length=50)),
                ('bookproperty_status', models.IntegerField(default=0)),
                ('bookproperty_sellproperty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Owner.tbl_sellproperty')),
                ('bookpropertyuser_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
