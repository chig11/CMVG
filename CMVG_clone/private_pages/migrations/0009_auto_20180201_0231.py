# Generated by Django 2.0.1 on 2018-02-01 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('private_pages', '0008_auto_20180131_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcements',
            name='creator_nickname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='cloudstorage',
            name='creator_nickname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='galleries',
            name='creator_nickname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='creator_full_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='cloudstorage',
            name='creator_full_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='galleries',
            name='creator_full_name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
