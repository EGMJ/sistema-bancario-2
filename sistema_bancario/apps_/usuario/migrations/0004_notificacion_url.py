# Generated by Django 2.1.7 on 2019-04-23 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_notificacion_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacion',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
