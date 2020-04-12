# Generated by Django 3.0.5 on 2020-04-10 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('title', models.TextField(primary_key=True, serialize=False)),
                ('director', models.CharField(max_length=200)),
                ('release_date', models.DateTimeField()),
                ('running_time', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('birth', models.DateTimeField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScreeningDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('finished_date', models.DateTimeField(null=True)),
                ('total_audience', models.IntegerField()),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Movie')),
            ],
        ),
    ]