# Generated by Django 5.1.7 on 2025-04-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_productmodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='weight',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='type',
            field=models.CharField(choices=[('Platinum', 'Platinum'), ('Gold', 'Gold'), ('Silver', 'Silver'), ('Bronze', 'Bronze')], max_length=50),
        ),
    ]
