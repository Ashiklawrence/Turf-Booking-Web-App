# Generated by Django 4.2.7 on 2024-01-16 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phno', models.IntegerField()),
                ('Username', models.CharField(max_length=100)),
                ('Password', models.IntegerField()),
            ],
        ),
    ]
