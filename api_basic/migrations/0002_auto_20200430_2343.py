# Generated by Django 3.0.5 on 2020-04-30 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date']},
        ),
    ]
