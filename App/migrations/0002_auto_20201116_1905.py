# Generated by Django 2.2 on 2020-11-16 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hobby',
            field=models.CharField(default='学生', max_length=64, verbose_name='兴趣爱好'),
        ),
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.CharField(max_length=62, null=True, verbose_name='个人简绍'),
        ),
    ]
