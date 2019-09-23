# Generated by Django 2.2 on 2019-06-26 16:57

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
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.TextField()),
                ('middlename', models.TextField()),
                ('surname', models.TextField()),
                ('contacts', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.TextField()),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('firstname', models.TextField()),
                ('middlename', models.TextField()),
                ('surname', models.TextField()),
                ('passport_number', models.TextField()),
                ('birth_date', models.DateField()),
                ('adress', models.TextField()),
                ('t_number', models.TextField()),
                ('education', models.CharField(choices=[('s', 'Начальное'), ('m', 'Среднее'), ('l', 'Высшее')], max_length=1)),
                ('hasDegree', models.BooleanField(default=False)),
                ('date_registration', models.DateField(auto_now_add=True)),
                ('date_out', models.DateField(default=None)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Employee')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.Room')),
            ],
        ),
    ]
