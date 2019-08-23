# Generated by Django 2.2.4 on 2019-08-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insured',
            name='insurance_ticket',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='insured',
            name='policy_number',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='insured',
            name='travel_assistance_voucher',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='insured',
            name='zurich_policy_number',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
