# Generated by Django 4.2.1 on 2023-06-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("pw", models.CharField(max_length=1000)),
                ("region", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=50)),
            ],
        ),
    ]
