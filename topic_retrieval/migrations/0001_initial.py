# Generated by Django 2.1.2 on 2018-12-26 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.CharField(max_length=19)),
                ('text', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
                ('url', models.CharField(blank=True, max_length=150)),
                ('first', models.BooleanField(default=False)),
            ],
        ),
    ]