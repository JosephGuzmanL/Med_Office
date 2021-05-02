# Generated by Django 3.2 on 2021-05-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='id',
        ),
        migrations.AddField(
            model_name='patient',
            name='identification',
            field=models.CharField(default='1', max_length=20, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]