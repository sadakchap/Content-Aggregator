# Generated by Django 2.2.3 on 2019-07-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src_name', models.CharField(max_length=255)),
                ('src_link', models.URLField()),
                ('title', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, upload_to='')),
                ('news_link', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
