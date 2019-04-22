# Generated by Django 2.1.5 on 2019-03-02 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_addprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100, null=True)),
                ('movie_image', models.ImageField(upload_to='')),
                ('movie_date', models.DateField()),
            ],
        ),
    ]