# Generated by Django 5.1.7 on 2025-03-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bloodrequest',
            options={'ordering': ['-urgency_level', 'created_at']},
        ),
        migrations.RemoveField(
            model_name='bloodrequest',
            name='location',
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='address',
            field=models.CharField(default='unknown', help_text='Enter the location for blood delivery or collection', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bloodrequest',
            name='urgency_level',
            field=models.IntegerField(choices=[(1, 'Low'), (2, 'Medium'), (3, 'High')], default=1),
        ),
    ]
