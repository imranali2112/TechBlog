# Generated by Django 5.0.4 on 2024-12-16 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CurdApp', '0005_employe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('decription', models.TextField()),
                ('dep', models.CharField(max_length=200)),
            ],
        ),
    ]