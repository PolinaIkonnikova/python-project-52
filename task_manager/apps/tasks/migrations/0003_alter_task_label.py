# Generated by Django 4.1.3 on 2022-11-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='label',
            field=models.ManyToManyField(null=True, through='tasks.LabelForTask', to='labels.label', verbose_name='Метки'),
        ),
    ]