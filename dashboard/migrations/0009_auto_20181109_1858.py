# Generated by Django 2.1.2 on 2018-11-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_remove_question_submitted_in_question_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='curriculum_followed',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='question',
            name='notes',
            field=models.CharField(default='', max_length=500),
        ),
    ]
