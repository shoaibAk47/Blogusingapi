# Generated by Django 3.0.5 on 2020-05-03 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api_basic', '0002_auto_20200430_2343'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
