# Generated by Django 2.2.4 on 2020-05-20 20:48

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('REItest', '0019_auto_20200520_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='bnt1',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bnt2',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bnt3',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='bnt4',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
    ]