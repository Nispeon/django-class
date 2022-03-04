# Generated by Django 4.0.3 on 2022-03-02 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.URLField(max_length=500)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.IntegerField(max_length=200)),
            ],
        ),
    ]
