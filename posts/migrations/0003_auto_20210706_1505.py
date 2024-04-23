# Generated by Django 3.2.5 on 2021-07-06 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='thumbail',
            new_name='thumbnail',
        ),
        migrations.AlterField(
            model_name='post',
            name='action_ip',
            field=models.CharField(editable=False, max_length=20, verbose_name='Posted IP'),
        ),
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, editable=False, verbose_name='Post Views'),
        ),
    ]
