# Generated by Django 4.2.6 on 2023-10-19 07:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='courseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('createat', models.DateTimeField(auto_now_add=True)),
                ('updateat', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='sessionYearModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionStart', models.CharField(max_length=100)),
                ('sessionEnd', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='studentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=100)),
                ('cratedat', models.DateTimeField(auto_now_add=True)),
                ('updateat', models.DateTimeField(auto_now=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('courseid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='student.coursemodel')),
                ('sessionyearid', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='student.sessionyearmodel')),
            ],
        ),
    ]