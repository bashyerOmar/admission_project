# Generated by Django 2.2.4 on 2022-06-26 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission_app', '0005_auto_20220626_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
