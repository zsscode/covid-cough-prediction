# Generated by Django 2.1.1 on 2020-04-05 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='location',
            new_name='city',
        ),
        migrations.AddField(
            model_name='response',
            name='age',
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='country',
            field=models.CharField(default='United States', max_length=200),
            preserve_default=False,
        ),
    ]