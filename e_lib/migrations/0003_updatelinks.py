# Generated by Django 3.0.7 on 2020-06-26 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_lib', '0002_auto_20200624_1550'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdateLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
