# Generated by Django 2.2.6 on 2019-12-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charapp', '0008_auto_20191203_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(),
        ),
    ]