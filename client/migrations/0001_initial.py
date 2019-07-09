# Generated by Django 2.2.3 on 2019-07-09 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('read_expire', models.BooleanField(default=True)),
                ('expiration', models.DateTimeField(null=True)),
            ],
        ),
    ]
