# Generated by Django 4.2.4 on 2023-09-04 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newspage", "0009_news_news_content_alter_news_news_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="news",
            name="news_content",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="news",
            name="news_title",
            field=models.CharField(max_length=30),
        ),
    ]
