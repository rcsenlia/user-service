# Generated by Django 4.1.3 on 2023-04-29 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Hobi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobi', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='nama',
        ),
        migrations.AddField(
            model_name='profile',
            name='deskripsi',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='domisili',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('P', 'P'), ('L', 'L')], max_length=1, null=True),
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='genre',
            field=models.ManyToManyField(to='profil.genre'),
        ),
        migrations.AddField(
            model_name='profile',
            name='hobi',
            field=models.ManyToManyField(to='profil.hobi'),
        ),
        migrations.AddField(
            model_name='profile',
            name='teman',
            field=models.ManyToManyField(related_name='teman', through='profil.Relationship', to=settings.AUTH_USER_MODEL),
        ),
    ]
