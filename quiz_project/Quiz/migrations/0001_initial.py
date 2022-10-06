# Generated by Django 4.1.1 on 2022-10-06 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultQuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('opt1', models.CharField(max_length=200, null=True)),
                ('opt2', models.CharField(max_length=200, null=True)),
                ('opt3', models.CharField(max_length=200, null=True)),
                ('opt4', models.CharField(max_length=200, null=True)),
                ('correct_ans', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OpenQuesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=250, null=True)),
                ('correct_ans', models.CharField(max_length=250)),
            ],
        ),
    ]