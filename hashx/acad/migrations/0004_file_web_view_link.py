# Generated by Django 3.0.5 on 2020-07-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0003_file_is_downloaded'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='web_view_link',
            field=models.URLField(max_length=150, null=True),
        ),
    ]