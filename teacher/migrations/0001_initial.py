# Generated by Django 3.0.5 on 2020-04-16 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('idc', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('emploi', models.FileField(blank=True, upload_to='emplois/%Y/%m/%D')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('mail', models.CharField(max_length=60)),
                ('cin', models.IntegerField(default=0)),
                ('classid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Class')),
            ],
        ),
    ]
