# Generated by Django 5.1.3 on 2025-01-09 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
                ('user_email', models.CharField(max_length=50)),
                ('user_contact', models.CharField(max_length=50)),
                ('user_address', models.CharField(max_length=50)),
                ('user_place', models.CharField(max_length=50)),
                ('user_photo', models.FileField(upload_to='Assets/user/photo')),
                ('user_password', models.CharField(max_length=50)),
            ],
        ),
    ]
