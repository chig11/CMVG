# Generated by Django 2.0.1 on 2018-02-28 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_pages', '0021_auto_20180227_0343'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
