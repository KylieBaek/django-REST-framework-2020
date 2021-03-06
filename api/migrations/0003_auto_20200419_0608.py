# Generated by Django 3.0.5 on 2020-04-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200415_0902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('EP', 'epic'), ('DS', 'disaster'), ('AC', 'action'), ('HR', 'horror'), ('FT', 'fantasy'), ('WR', 'war'), ('CM', 'comedy'), ('SF', 'science_fiction'), ('RM', 'romance'), ('WS', 'western'), ('TH', 'thriller'), ('DC', 'documentary'), ('AD', 'adventure'), ('SP', 'sport'), ('MS', 'mystery'), ('DR', 'drama'), ('MU', 'musical')], max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='nickname',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='rank',
            field=models.CharField(choices=[('V', 'vip'), ('S', 'silver'), ('G', 'gold')], max_length=10),
        ),
        migrations.AlterField(
            model_name='workers',
            name='position',
            field=models.CharField(blank=True, choices=[('TK', 'ticket'), ('CO', 'counter'), ('CL', 'cleaning'), ('FD', 'food')], max_length=10, null=True),
        ),
    ]
