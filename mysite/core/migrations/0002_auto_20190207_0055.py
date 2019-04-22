# Generated by Django 2.1.5 on 2019-02-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=16)),
                ('companyimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
