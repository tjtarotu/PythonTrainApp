# Generated by Django 2.0 on 2017-12-24 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('train_bot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('station', models.CharField(max_length=100)),
                ('geo_lon', models.DecimalField(decimal_places=2, max_digits=12)),
                ('geo_lat', models.DecimalField(decimal_places=2, max_digits=12)),
                ('railway', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train_bot.Railway')),
            ],
        ),
    ]
