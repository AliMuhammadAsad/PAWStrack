# Generated by Django 5.0.4 on 2024-04-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_pet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='adoption_history',
            field=models.TextField(default='Never Adopted'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='picture',
            field=models.ImageField(default='default.png', upload_to='pets/'),
        ),
        migrations.AlterField(
            model_name='pet',
            name='treatment_costs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]