# Generated by Django 4.1.1 on 2022-10-07 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0014_listing_watcher"),
    ]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]