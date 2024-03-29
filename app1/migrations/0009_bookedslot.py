# Generated by Django 4.2.7 on 2024-02-02 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_slot_bookdate_alter_slot_bookedby'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookedSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bookingid', models.TextField()),
                ('Slotname', models.CharField(max_length=50)),
                ('Timerange', models.TextField()),
                ('Booked', models.BooleanField(default=False)),
                ('Bookedby', models.TextField()),
                ('Bookdate', models.TextField()),
                ('Slotdate', models.TextField()),
            ],
        ),
    ]
