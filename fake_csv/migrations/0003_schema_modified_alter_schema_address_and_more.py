# Generated by Django 4.1.3 on 2022-12-04 22:54

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("fake_csv", "0002_schema"),
    ]

    operations = [
        migrations.AddField(
            model_name="schema",
            name="modified",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="schema",
            name="address",
            field=models.CharField(default="Centralna 132", max_length=255),
        ),
        migrations.AlterField(
            model_name="schema",
            name="company",
            field=models.CharField(default="Xiaomi", max_length=30),
        ),
        migrations.AlterField(
            model_name="schema",
            name="date",
            field=models.DateField(default=datetime.datetime(2008, 6, 13, 4, 15, 9)),
        ),
        migrations.AlterField(
            model_name="schema",
            name="full_name",
            field=models.CharField(default="Danylo Sagaydachny", max_length=255),
        ),
        migrations.AlterField(
            model_name="schema",
            name="phone",
            field=models.CharField(default="+48633285674", max_length=14),
        ),
        migrations.AlterField(
            model_name="schema",
            name="text",
            field=models.TextField(
                default="fghlighlsdifughsidfuhgsdifghsdifghsidfhgsdifuhgsidfuhgsidufhgsdg"
            ),
        ),
    ]
