# Generated by Django 3.0.8 on 2020-07-29 11:28

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('acad', '0006_auto_20200728_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('ODD', 'ODD'), ('EVEN', 'EVEN')], max_length=4)),
            ],
        ),
    ]