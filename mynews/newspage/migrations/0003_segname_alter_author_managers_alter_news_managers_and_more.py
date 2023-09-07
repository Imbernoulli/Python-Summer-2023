# Generated by Django 4.2.4 on 2023-09-02 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("newspage", "0002_alter_author_managers_alter_news_managers_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="SegName",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("seg_name", models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterModelManagers(
            name="author",
            managers=[],
        ),
        migrations.AlterModelManagers(
            name="news",
            managers=[],
        ),
        migrations.RenameField(
            model_name="news",
            old_name="num_read",
            new_name="news_popularity",
        ),
        migrations.RemoveField(
            model_name="news",
            name="news_content",
        ),
        migrations.AddField(
            model_name="author",
            name="author_fans",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="news",
            name="news_id",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="author",
            name="author_name",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="news",
            name="news_title",
            field=models.CharField(max_length=30),
        ),
        migrations.CreateModel(
            name="Segcontent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score", models.FloatField()),
                (
                    "its_article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="segcontents",
                        to="newspage.news",
                    ),
                ),
                (
                    "its_seg",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="newspage.news"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Keywords",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("word_name", models.CharField(max_length=8)),
                ("its_article", models.ManyToManyField(to="newspage.news")),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("its_author", models.IntegerField()),
                ("comment_user", models.CharField(max_length=30)),
                ("comment_content", models.TextField()),
                (
                    "its_article",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="newspage.news"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="news",
            name="its_keywords",
            field=models.ManyToManyField(to="newspage.keywords"),
        ),
    ]
