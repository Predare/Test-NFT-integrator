# Generated by Django 4.0.3 on 2022-04-01 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='token',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='token',
            name='owner',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='token',
            name='tx_hash',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='token',
            name='unique_hash',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]