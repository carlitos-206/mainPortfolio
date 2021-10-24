# Generated by Django 2.2 on 2021-10-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='device_count',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=255)),
                ('ticket_id', models.CharField(max_length=255)),
                ('is_bot', models.BooleanField(default=False)),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('latitude', models.CharField(max_length=255)),
                ('longitude', models.CharField(max_length=255)),
                ('device_name', models.CharField(max_length=255)),
                ('device_family', models.CharField(max_length=255)),
                ('device_type', models.CharField(max_length=255)),
                ('device_os', models.CharField(max_length=255)),
                ('touch_capability', models.BooleanField(default=False)),
                ('device_count', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]