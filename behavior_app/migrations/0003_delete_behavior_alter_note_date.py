# Generated by Django 4.2.3 on 2023-07-21 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('behavior_app', '0002_alter_note_behavior_alter_note_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Behavior',
        ),
        migrations.AlterField(
            model_name='note',
            name='date',
            field=models.DateField(),
        ),
    ]
