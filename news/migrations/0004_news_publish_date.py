# Generated by Django 3.1.2 on 2020-10-12 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20201012_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='publish_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
