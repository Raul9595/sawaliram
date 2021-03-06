# Generated by Django 2.1.5 on 2019-05-14 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_answer_approved_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnencodedSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_questions', models.IntegerField()),
                ('excel_sheet_name', models.CharField(max_length=100)),
                ('encoded', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'unencoded_submission',
            },
        ),
        migrations.RenameField(
            model_name='uncuratedsubmission',
            old_name='excel_sheet',
            new_name='excel_sheet_name',
        ),
        migrations.AddField(
            model_name='question',
            name='encoded_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='encoded_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
