# Generated by Django 2.2.6 on 2019-10-26 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campesinos', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='campesino',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='campesinos.Campesino'),
        ),
    ]
