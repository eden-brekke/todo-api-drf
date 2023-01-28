# Generated by Django 4.1.5 on 2023-01-28 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('priority', models.IntegerField(default=1)),
                ('completed', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
