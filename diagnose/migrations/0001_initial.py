# Generated by Django 4.1 on 2023-08-10 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Answer",
            fields=[
                ("answerpk", models.AutoField(primary_key=True, serialize=False)),
                ("answer", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "answer",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Checkans",
            fields=[
                ("checkanspk", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "checkans",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Checklist",
            fields=[
                ("checklistpk", models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                "db_table": "checklist",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Format",
            fields=[
                ("formatpk", models.AutoField(primary_key=True, serialize=False)),
                ("format", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "format",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="List",
            fields=[
                ("listpk", models.AutoField(primary_key=True, serialize=False)),
                ("question", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "list",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Session",
            fields=[
                ("sessionpk", models.AutoField(primary_key=True, serialize=False)),
                ("userid", models.CharField(max_length=255)),
                ("snow", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "session",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Site",
            fields=[
                ("sitepk", models.AutoField(primary_key=True, serialize=False)),
                ("site", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "site",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Version",
            fields=[
                ("versionpk", models.AutoField(primary_key=True, serialize=False)),
                ("vnow", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "db_table": "version",
                "managed": False,
            },
        ),
    ]
