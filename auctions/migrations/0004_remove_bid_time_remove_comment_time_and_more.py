# Generated by Django 4.1.1 on 2022-10-05 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0003_alter_listing_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="bid",
            name="time",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="time",
        ),
        migrations.RemoveField(
            model_name="listing",
            name="time",
        ),
    ]