# Generated by Django 3.0.5 on 2020-05-05 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0005_auto_20200506_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holidays',
            name='name',
            field=models.TextField(),
        ),
    ]