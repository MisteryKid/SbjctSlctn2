# Generated by Django 3.2.4 on 2021-06-03 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('clsNb', models.IntegerField(max_length=5)),
                ('Name', models.CharField(max_length=10)),
                ('pw', models.IntegerField(max_length=4)),
            ],
        ),
    ]
