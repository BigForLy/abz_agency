# Generated by Django 4.0.4 on 2022-05-16 07:57

from django.db import migrations, models
import staff.models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_alter_staff_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(max_length=254, null=True, upload_to=staff.models.upload_to),
        ),
    ]
