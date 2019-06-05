# Generated by Django 2.1.3 on 2018-12-06 23:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('classes_ownership', models.ManyToManyField(blank=True, related_name='owner_classe', to='student.Classes')),
                ('sections_ownership', models.ManyToManyField(blank=True, related_name='owner_section', to='student.Sections')),
            ],
            options={
                'verbose_name_plural': "User's details",
                'verbose_name': "User's detail",
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='user_details',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]