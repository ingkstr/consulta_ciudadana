# Generated by Django 2.2.9 on 2020-01-06 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0002_voter_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='polls',
            field=models.ManyToManyField(to='administration.Poll'),
        ),
    ]
