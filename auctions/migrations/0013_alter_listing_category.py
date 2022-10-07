# Generated by Django 4.1.1 on 2022-10-07 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0012_rename_starting_price_listing_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="category",
            field=models.CharField(
                choices=[
                    ("Clothing/Footwear", "Clothing/Footwear"),
                    ("Books", "Books"),
                    ("Electronics", "Electronics"),
                    ("Cosmetics", "Cosmetics"),
                    ("Toys", "Toys"),
                    ("Home/Garden", "Home/Garden"),
                    ("Sport/Leisure", "Sport/Leisure"),
                    ("Other", "Other"),
                ],
                max_length=32,
            ),
        ),
    ]
