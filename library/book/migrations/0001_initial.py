# Generated by Django 3.1.2 on 2020-10-29 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(default='Anonymous', max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('describe', models.TextField(default='Dataflair Django Tutorial')),
            ],
        ),
    ]
