# Generated by Django 2.2 on 2019-09-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Name of the event', max_length=255)),
                ('event_description', models.TextField()),
                ('guests', models.TextField(blank=True, help_text='name of outides attendees')),
            ],
        ),
    ]
