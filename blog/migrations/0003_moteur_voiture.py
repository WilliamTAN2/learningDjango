# Generated by Django 2.0.6 on 2018-06-15 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180615_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moteur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Voiture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('moteur', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.Moteur')),
            ],
        ),
    ]
