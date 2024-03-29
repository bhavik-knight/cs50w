# Generated by Django 4.0.2 on 2022-02-25 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrivals', to='flights.airport'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departures', to='flights.airport'),
        ),
    ]
