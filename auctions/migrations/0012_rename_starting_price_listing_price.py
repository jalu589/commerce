# Generated by Django 4.1.1 on 2022-10-07 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0011_alter_listing_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="listing",
            old_name="starting_price",
            new_name="price",
        ),
    ]
