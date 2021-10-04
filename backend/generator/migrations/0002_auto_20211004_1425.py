# Generated by Django 3.2.7 on 2021-10-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='completedquote',
            old_name='font',
            new_name='font_family',
        ),
        migrations.RemoveField(
            model_name='completedquote',
            name='tweet',
        ),
        migrations.AddField(
            model_name='completedquote',
            name='font_style',
            field=models.CharField(default='bold', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='completedquote',
            name='font_weight',
            field=models.CharField(default='str', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='completedquote',
            name='quote',
            field=models.CharField(default='str', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='completedquote',
            name='picture_url',
            field=models.CharField(max_length=200),
        ),
    ]
