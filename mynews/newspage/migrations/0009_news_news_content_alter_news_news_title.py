# Generated by Django 4.2.4 on 2023-09-04 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newspage", "0008_remove_segcontent_ranking"),
    ]

    operations = [
        migrations.AddField(
            model_name="news",
            name="news_content",
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="news",
            name="news_title",
            field=models.TextField(),
        ),
    ]
