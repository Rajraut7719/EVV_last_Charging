# Generated by Django 3.2.13 on 2022-06-29 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_management', '0002_alter_user_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(help_text='Enter mobile no', max_length=14),
        ),
    ]
