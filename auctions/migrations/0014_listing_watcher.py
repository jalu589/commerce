# Generated by Django 4.1.1 on 2022-10-07 22:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0013_alter_listing_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="watcher",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]