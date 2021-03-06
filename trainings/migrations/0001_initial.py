# Generated by Django 3.2 on 2021-04-10 10:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('team', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='kategoria')),
            ],
            options={
                'verbose_name': 'Kategoria wiekowa',
                'verbose_name_plural': 'Kategoria wiekowa',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('techniqe', 'Technika'), ('tactics', 'Taktyka'), ('motorics', 'Motoryka'), ('other', 'Inna')], default='other', max_length=20, verbose_name='kategoria')),
                ('title', models.CharField(blank=True, default='', max_length=250, verbose_name='Tytuł')),
                ('description', models.TextField(blank=True, default='', verbose_name='opis')),
                ('duration', models.IntegerField(blank=True, default='', verbose_name='czas trwania')),
                ('age_category', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='trainings.agecategory')),
                ('author', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='autor', to=settings.AUTH_USER_MODEL, verbose_name='autor')),
            ],
            managers=[
                ('techniqe', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=250, verbose_name='Tytuł')),
                ('date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Data i godzina')),
                ('duration', models.IntegerField(blank=True, default='90', verbose_name='Czas trwania')),
                ('place', models.TextField(blank=True, verbose_name='Miejsce')),
                ('type', models.CharField(choices=[('training', 'Trening'), ('match', 'Mecz'), ('meeting', 'Spotkanie')], default='training', max_length=10, verbose_name='Typ')),
                ('content', models.TextField(blank=True, default='', verbose_name='Treść')),
                ('summary', models.TextField(blank=True, default='', verbose_name='Podsumowanie')),
                ('author', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainings_created', to='user.coach', verbose_name='autor')),
                ('participants', models.ManyToManyField(blank=True, default='', related_name='trainings', to='user.Player', verbose_name='Uczestnicy')),
                ('performer', models.ManyToManyField(blank=True, default='', related_name='trainings_performed', to='user.Coach', verbose_name='Wykonawca')),
                ('team', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trainings', to='team.team', verbose_name='Zespół')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='autor')),
                ('event', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='trainings.event', verbose_name='wydarzenie')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ('created',),
            },
        ),
    ]
