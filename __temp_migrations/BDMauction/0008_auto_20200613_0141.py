# Generated by Django 2.2.4 on 2020-06-13 00:41

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('BDMauction', '0007_auto_20200613_0135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='cq_a1',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '$25'], [2, '$35'], [3, '$16'], [4, 'None of the above']], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='cq_a2',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '$25'], [2, '$35'], [3, '$31'], [4, '$21']], null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='cq_a3',
            field=otree.db.models.PositiveIntegerField(choices=[[1, '$25'], [2, '$35'], [3, '$31'], [4, '$21']], null=True),
        ),
    ]
