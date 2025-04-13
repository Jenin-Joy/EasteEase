# Generated by Django 5.1.3 on 2025-02-20 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_tbl_owner_owner_status'),
        ('Owner', '0006_tbl_sellproperty'),
        ('User', '0002_tbl_complaint'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_bookproperty',
            old_name='bookproperty_user_id',
            new_name='bookpropertyuser_id',
        ),
        migrations.CreateModel(
            name='tbl_rentbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rentbooking_id', models.CharField(max_length=50)),
                ('rentbooking_amount', models.CharField(max_length=50)),
                ('rentbooking_date', models.DateField()),
                ('rentproperty_status', models.IntegerField(default=0)),
                ('rentproperty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Owner.tbl_rentproperty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
