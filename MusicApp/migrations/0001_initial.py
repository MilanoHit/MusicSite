# Generated by Django 4.2.3 on 2023-08-08 11:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^[a-zA-Z0-9_]*$')])),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('pop music', 'Pop Music'), ('jazz music', 'Jazz Music'), ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Metal Music', 'Metal Music'), ('Other', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=30)),
                ('image', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicApp.profile')),
            ],
        ),
    ]
