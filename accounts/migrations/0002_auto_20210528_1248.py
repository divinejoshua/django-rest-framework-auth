# Generated by Django 3.2.3 on 2021-05-28 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='first_name',
            field=models.CharField(blank=True, default='user firstname', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='fullname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='last_name',
            field=models.CharField(blank=True, default='user lastname', max_length=30, null=True),
        ),
    ]
