# Generated by Django 5.1.2 on 2024-10-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('bug', 'Bug'), ('feature', 'Feature'), ('support', 'Support')], max_length=50)),
                ('priority', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=50)),
                ('contact_info', models.EmailField(max_length=254)),
            ],
        ),
    ]