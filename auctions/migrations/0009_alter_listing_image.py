# Generated by Django 4.1.1 on 2022-10-06 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0008_alter_listing_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="image",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]