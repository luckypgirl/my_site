# Generated by Django 2.2 on 2019-04-11 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190410_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='contents',
            field=models.TextField(verbose_name='内容'),
        ),
    ]
