# Generated by Django 2.2.12 on 2022-02-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('providers', '0007_providergame_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='providercover',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='providergenre',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='providerplatform',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
