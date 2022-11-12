# Generated by Django 4.1.1 on 2022-10-15 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_remove_label_tasks_delete_taskship'),
        ('tasks', '0003_alter_task_status_labelfortask_task_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labelfortask',
            name='label',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='labels.label'),
        ),
        migrations.AlterField(
            model_name='labelfortask',
            name='task',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to='tasks.task'),
        ),
    ]
