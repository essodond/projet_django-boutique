# Generated by Django 5.1.4 on 2025-02-09 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vente',
            name='produit_nom',
            field=models.CharField(default='Default Product Name', max_length=100),
        ),
        migrations.AddField(
            model_name='vente',
            name='quantite',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
