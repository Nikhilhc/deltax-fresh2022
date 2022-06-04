# Generated by Django 4.0.5 on 2022-06-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('bio', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_of_release', models.DateField()),
                ('cover_image', models.ImageField(upload_to='uploads/')),
                ('rating', models.IntegerField()),
                ('artists', models.ManyToManyField(blank=True, null=True, to='deltax_frontend.artists')),
            ],
        ),
    ]
