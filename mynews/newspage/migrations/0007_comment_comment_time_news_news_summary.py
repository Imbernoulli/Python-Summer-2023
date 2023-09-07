# Generated by Django 4.2.4 on 2023-09-03 10:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newspage", "0006_alter_segcontent_its_article"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="comment_time",
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name="news",
            name="news_summary",
            field=models.CharField(default=0, max_length=60),
            preserve_default=False,
        ),
    ]
