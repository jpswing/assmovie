# Generated by Django 2.0.4 on 2019-09-15 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('expire_time', models.DateTimeField()),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Cinema')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'coupon',
            },
        ),
    ]
