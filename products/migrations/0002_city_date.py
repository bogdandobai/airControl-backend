# Generated by Django 3.0.2 on 2020-04-11 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
