# Generated by Django 4.1.1 on 2022-10-12 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0016_remove_listing_watcher_listing_watchers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="commenter",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="my_comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
