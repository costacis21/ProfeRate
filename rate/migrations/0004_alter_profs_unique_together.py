# Generated by Django 4.0.3 on 2022-03-21 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0003_profs_name_code_alter_modules_semester_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='profs',
            unique_together={('full_name', 'name_code')},
        ),
    ]
