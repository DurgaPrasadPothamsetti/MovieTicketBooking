# Generated by Django 2.1.5 on 2019-02-28 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20190228_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]