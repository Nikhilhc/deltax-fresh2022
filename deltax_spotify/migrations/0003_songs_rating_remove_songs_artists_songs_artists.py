# Generated by Django 4.0.5 on 2022-06-04 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deltax_spotify', '0002_songs_artists'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='songs',
            name='artists',
        ),
        migrations.AddField(
            model_name='songs',
            name='artists',
            field=models.ManyToManyField(blank=True, null=True, to='deltax_spotify.artists'),
        ),
    ]
