# Generated by Django 3.0.3 on 2020-09-13 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200912_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]