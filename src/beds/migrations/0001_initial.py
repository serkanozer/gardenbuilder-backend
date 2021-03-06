# Generated by Django 3.1 on 2020-09-21 19:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gardens', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now)),
                ('length', models.PositiveSmallIntegerField(default=0)),
                ('width', models.PositiveSmallIntegerField(default=0)),
                ('notes', models.CharField(max_length=500)),
                ('garden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beds', to='gardens.garden')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
