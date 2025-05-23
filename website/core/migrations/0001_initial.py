# Generated by Django 5.1.7 on 2025-04-12 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_image_1', models.ImageField(blank=True, null=True, upload_to='core/cloth/first')),
                ('cloth_image_2', models.ImageField(blank=True, null=True, upload_to='core/cloth/second')),
                ('cloth_name', models.CharField(max_length=200)),
                ('cloth_price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'cloth',
                'verbose_name_plural': 'clothes',
            },
        ),
        migrations.CreateModel(
            name='headphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headphone_image', models.ImageField(blank=True, null=True, upload_to='core/headphone')),
                ('headphone_name', models.CharField(max_length=200)),
                ('headphone_price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'headphone',
                'verbose_name_plural': 'headphones',
            },
        ),
        migrations.CreateModel(
            name='watch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watch_image', models.ImageField(blank=True, null=True, upload_to='core/watch')),
                ('watch_name', models.CharField(max_length=200)),
                ('watch_price', models.IntegerField()),
            ],
            options={
                'verbose_name': 'watch',
                'verbose_name_plural': 'watches',
            },
        ),
    ]
