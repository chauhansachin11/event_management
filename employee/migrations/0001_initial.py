# Generated by Django 3.2.4 on 2023-09-19 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('emp_id', models.IntegerField()),
                ('salary', models.FloatField()),
                ('city', models.CharField(max_length=100)),
            ],
        ),
    ]