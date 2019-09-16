# Generated by Django 2.0.4 on 2019-09-15 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'actor',
            },
        ),
        migrations.CreateModel(
            name='ActorMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Actor')),
            ],
            options={
                'db_table': 'actor_movie',
            },
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cinema',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('onshow', models.BooleanField()),
                ('wanted', models.IntegerField()),
                ('show_time', models.DateField()),
                ('poster_img', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'movie',
            },
        ),
        migrations.CreateModel(
            name='RateRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=1, max_digits=2)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.User')),
            ],
            options={
                'db_table': 'rate_record',
            },
        ),
        migrations.CreateModel(
            name='ShowRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('room', models.CharField(max_length=100)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Cinema')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
            options={
                'db_table': 'show_record',
            },
        ),
        migrations.AddField(
            model_name='actormovie',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actors', to='movie.Movie'),
        ),
    ]
