# Generated by Django 3.2.10 on 2023-05-11 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentencedata',
            fields=[
                ('idsentencedata', models.IntegerField(db_column='idsentenceData', primary_key=True, serialize=False)),
                ('sentencedata_contents', models.CharField(db_column='sentenceData_contents', max_length=200)),
                ('sentencedata_word1', models.CharField(db_column='sentenceData_word1', max_length=45)),
                ('sentencedata_word2', models.CharField(db_column='sentenceData_word2', max_length=45)),
                ('sentencedata_word3', models.CharField(db_column='sentenceData_word3', max_length=45)),
                ('sentencedata_word4', models.CharField(db_column='sentenceData_word4', max_length=45)),
                ('sentencedata_answerword', models.CharField(db_column='sentenceData_answerword', max_length=45)),
            ],
            options={
                'db_table': 'sentenceData',
                'managed': False,
            },
        ),
    ]