# Generated by Django 2.2.4 on 2020-06-15 12:55

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('cognitivenoise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='feedback_general',
        ),
        migrations.RemoveField(
            model_name='player',
            name='feedback_p1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='feedback_p2',
        ),
        migrations.RemoveField(
            model_name='player',
            name='feedback_p3',
        ),
        migrations.AlterField(
            model_name='player',
            name='decmode',
            field=otree.db.models.PositiveIntegerField(choices=[[7, 'Almost always (near 100% of the time)'], [6, 'Very often (about 80% of the time)'], [5, 'Moderately often (about 60% of the time)'], [4, 'About half of the time (50% of the time)'], [3, 'Moderately seldom (about 40% of the time)'], [2, 'Very seldom (about 20% of the time)'], [1, 'Almost never (near 0% of the time)']], null=True),
        ),
    ]