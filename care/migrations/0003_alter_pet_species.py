# Generated by Django 5.0.7 on 2024-11-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0002_pet_species'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='species',
            field=models.CharField(blank=True, choices=[('Dog', 'Dog'), ('Cat', 'Cat'), ('Bird', 'Bird'), ('Fish', 'Fish'), ('Snake', 'Snake')], max_length=100, null=True),
        ),
    ]
