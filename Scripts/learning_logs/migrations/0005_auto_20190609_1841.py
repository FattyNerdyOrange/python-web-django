# Generated by Django 2.2.2 on 2019-06-09 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name_plural': 'comments'},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='topic',
        ),
    ]
