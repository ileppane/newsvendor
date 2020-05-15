# Generated by Django 2.2.4 on 2020-05-15 00:56

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('REItest', '0004_auto_20200515_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='crt4',
            field=otree.db.models.StringField(choices=[('4 days', '4 days'), ('9 days', '9 days'), ('12 days', '12 days'), ('3 days', '3 days')], max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='crt5',
            field=otree.db.models.StringField(choices=[('29 students', '29 students'), ('30 students', '30 students'), ('1 student', '1 student'), ('15 students', '15 students')], max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='crt6',
            field=otree.db.models.StringField(choices=[('20 pounds', '20 pounds'), ('10 pounds', '10 pounds'), ('0 pounds', '0 pounds'), ('30 pounds', '30 pounds')], max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='crt7',
            field=otree.db.models.StringField(choices=[('has lost money.', 'has lost money.'), ('is ahead of where he began.', 'is ahead of where he began.'), ('has broken even in the stock market.', 'has broken even in the stock market.'), ('it cannot be determined.', 'it cannot be determined.')], max_length=10000, null=True),
        ),
    ]
