# Generated by Django 4.0.1 on 2022-01-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sarlavha', models.CharField(max_length=200)),
                ('Matn', models.TextField()),
            ],
        ),
    ]
