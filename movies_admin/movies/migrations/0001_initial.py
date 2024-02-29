# Generated by Django 4.2.5 on 2024-02-29 20:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [

        migrations.CreateModel(
            name='Filmwork',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('creation_date', models.CharField(blank=True, db_index=True, null=True, verbose_name='year_of_release')),
                ('rating', models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='rating')),
                ('type', models.CharField(choices=[('movie', 'movie'), ('tv_show', 'tv_show')], default='movie', verbose_name='type')),
            ],
            options={
                'verbose_name': 'film work',
                'verbose_name_plural': 'film works',
                'db_table': 'content"."film_work',
                'ordering': ['-creation_date'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='genre')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
            ],
            options={
                'verbose_name': 'genre',
                'verbose_name_plural': 'genres',
                'db_table': 'content"."genre',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_date')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=255, verbose_name='full name')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
                'db_table': 'content"."person',
                'ordering': ['full_name'],
            },
        ),
        migrations.CreateModel(
            name='PersonFilmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('role', models.TextField(choices=[('actor', 'actor'), ('director', 'director'), ('writer', 'writer')], default='actor', verbose_name='role')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.person', verbose_name='person')),
            ],
            options={
                'verbose_name': ('person film work',),
                'db_table': 'content"."person_film_work',
            },
        ),
        migrations.CreateModel(
            name='GenreFilmwork',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('film_work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.filmwork')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.genre', verbose_name='genre')),
            ],
            options={
                'verbose_name': 'genre film work',
                'db_table': 'content"."genre_film_work',
            },
        ),
        migrations.AddIndex(
            model_name='genre',
            index=models.Index(fields=['-name'], name='genre_name_464984_idx'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='genre',
            field=models.ManyToManyField(through='movies.GenreFilmwork', to='movies.genre'),
        ),
        migrations.AddField(
            model_name='filmwork',
            name='person',
            field=models.ManyToManyField(through='movies.PersonFilmwork', to='movies.person'),
        ),
        migrations.AddConstraint(
            model_name='personfilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'person', 'role'), name='unique_filmwork_preson_role'),
        ),
        migrations.AddConstraint(
            model_name='genrefilmwork',
            constraint=models.UniqueConstraint(fields=('film_work', 'genre'), name='unique_filmwork_genre'),
        ),
        migrations.AddIndex(
            model_name='filmwork',
            index=models.Index(fields=['creation_date'], name='film_work_creatio_02a6ad_idx'),
        ),
    ]
