# Generated by Django 4.2.7 on 2024-02-12 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='Bookdate',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='Booked',
        ),
        migrations.RemoveField(
            model_name='slot',
            name='Bookedby',
        ),
    ]
