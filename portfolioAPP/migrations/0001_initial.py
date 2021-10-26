# Generated by Django 2.2 on 2021-10-26 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flagged', models.BooleanField(default=False)),
                ('source', models.CharField(max_length=100)),
                ('ticket_id', models.CharField(max_length=255)),
                ('ip', models.CharField(blank=True, max_length=64, null=True)),
                ('is_bot', models.CharField(default='False', max_length=255)),
                ('visit_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='locations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('lat', models.CharField(max_length=255, null=True)),
                ('lon', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('this_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='l_ticket', to='portfolioAPP.users')),
            ],
        ),
        migrations.CreateModel(
            name='devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('family', models.CharField(max_length=255)),
                ('os', models.CharField(max_length=255)),
                ('touch_capability', models.BooleanField(default=False)),
                ('browser_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('this_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='d_ticket', to='portfolioAPP.users')),
            ],
        ),
    ]
