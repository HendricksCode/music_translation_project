# Generated by Django 2.0.7 on 2022-06-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translate',
            name='French',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='translate',
            name='German',
            field=models.CharField(blank=True, max_length=120),
        ),
        migrations.AlterField(
            model_name='translate',
            name='Italian',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]