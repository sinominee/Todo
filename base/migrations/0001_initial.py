# Generated by Django 5.0 on 2024-01-01 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('Done', 'Done'), ('In progress', 'In progress'), ('Not done', 'Not done')], default='In progress', max_length=50)),
            ],
        ),
    ]
