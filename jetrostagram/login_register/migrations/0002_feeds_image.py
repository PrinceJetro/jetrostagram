# Generated by Django 4.1.7 on 2023-03-31 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeds',
            name='image',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
    ]
