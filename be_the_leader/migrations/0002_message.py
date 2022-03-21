# Generated by Django 4.0.2 on 2022-03-12 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('be_the_leader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
    ]
