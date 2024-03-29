# Generated by Django 3.2 on 2021-05-08 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20210508_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('presentation', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddConstraint(
            model_name='medicine',
            constraint=models.UniqueConstraint(fields=('name', 'presentation'), name='constraint_medicine'),
        ),
    ]
