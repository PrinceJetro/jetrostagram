# Generated by Django 4.1.7 on 2023-04-01 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0011_update_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update_pic',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]