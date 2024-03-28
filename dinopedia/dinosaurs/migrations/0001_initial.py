# Generated by Django 4.2.2 on 2023-06-08 09:52

import colorfield.fields
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dinosaur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('eating_classification', models.CharField(choices=[('carnivores', 'Carnivores'), ('herbivores', 'Herbivores'), ('omnivores', 'Omnivores')], max_length=30)),
                ('typical_color', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None)),
                ('period_lived', models.CharField(choices=[('triassic', 'Triassic'), ('jurassic', 'Jurassic'), ('cretaceous', 'Cretaceous'), ('paleogene', 'Paleogene'), ('neogene', 'Neogene')], max_length=30)),
                ('average_size', models.CharField(choices=[('tiny', 'Tiny: Less than 1 meter in length'), ('very_small', 'Very Small: 1-2 meters in length'), ('small', 'Small: 2-4 meters in length'), ('medium', 'Medium: 4-8 meters in length'), ('large', 'Large: 8-15 meters in length'), ('very_large', 'Very Large: More than 15 meters in length')], max_length=30)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='dinosaurs/photos')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False)),
                ('dinosaur', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='photos', to='dinosaurs.dinosaur')),
            ],
        ),
        migrations.AddIndex(
            model_name='dinosaur',
            index=django.contrib.postgres.indexes.HashIndex(fields=['eating_classification'], name='dinosaurs_d_eating__4df570_hash'),
        ),
        migrations.AddIndex(
            model_name='dinosaur',
            index=django.contrib.postgres.indexes.HashIndex(fields=['period_lived'], name='dinosaurs_d_period__7c5b52_hash'),
        ),
        migrations.AddIndex(
            model_name='dinosaur',
            index=django.contrib.postgres.indexes.HashIndex(fields=['average_size'], name='dinosaurs_d_average_bb55a2_hash'),
        ),
    ]