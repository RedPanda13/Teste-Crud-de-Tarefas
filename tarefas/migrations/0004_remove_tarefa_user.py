# Generated by Django 3.0.4 on 2020-03-13 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0003_auto_20200313_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='user',
        ),
    ]