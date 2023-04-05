# Generated by Django 4.1.7 on 2023-03-31 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0003_uploadimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImagefieldModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'imageupload',
            },
        ),
        migrations.DeleteModel(
            name='UploadImage',
        ),
    ]
