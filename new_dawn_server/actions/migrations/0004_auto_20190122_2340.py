# Generated by Django 2.1.3 on 2019-01-23 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0003_auto_20190122_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertouseractionmetadata',
            name='entity_type',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
