# Generated by Django 2.2 on 2019-06-26 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_remove_reader_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='date_out',
            field=models.DateField(default=None, null=True),
        ),
    ]
