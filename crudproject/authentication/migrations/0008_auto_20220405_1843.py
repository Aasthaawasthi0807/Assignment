# Generated by Django 3.0.14 on 2022-04-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_auto_20220405_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(default='', max_length=30),
        ),
    ]