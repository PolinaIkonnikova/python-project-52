# Generated by Django 4.1.3 on 2022-11-15 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': 'Метка', 'verbose_name_plural': 'Метки'},
        ),
    ]
