# Generated by Django 5.0.4 on 2024-04-21 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_contactmessage_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
