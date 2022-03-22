# Generated by Django 4.0.3 on 2022-03-22 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0004_alter_profs_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratings',
            name='profs',
        ),
        migrations.AddField(
            model_name='ratings',
            name='profs',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='rate.profs'),
            preserve_default=False,
        ),
    ]
