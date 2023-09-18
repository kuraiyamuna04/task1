# Generated by Django 4.2.5 on 2023-09-18 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorialapp', '0003_user_delete_mymodel_delete_secondmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='SecondModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
