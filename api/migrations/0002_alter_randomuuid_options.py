# Generated by Django 4.0.1 on 2022-01-16 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='randomuuid',
            options={'ordering': ('-created_on',)},
        ),
    ]
