# Generated by Django 5.1.3 on 2025-02-27 09:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_tbl_owner_owner_status'),
        ('Owner', '0010_tbl_rentproperty'),
        ('User', '0010_delete_tbl_rentbooking'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_rentbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rentbooking_date', models.DateField(auto_now_add=True)),
                ('rentbooking_amount', models.CharField(max_length=50)),
                ('rentproperty_status', models.IntegerField(default=0)),
                ('rentbooking_fdate', models.DateField()),
                ('rentbooking_tdate', models.DateField()),
                ('rentproperty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Owner.tbl_rentproperty')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
