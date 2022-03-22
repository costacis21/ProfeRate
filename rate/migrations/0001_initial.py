# Generated by Django 4.0.3 on 2022-03-21 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_by', models.CharField(max_length=10, verbose_name='Module abbreviation')),
                ('full_name', models.CharField(max_length=20, verbose_name="Module's full name")),
                ('semester', models.IntegerField(max_length=1, verbose_name='Semester this module is being taught')),
                ('year', models.IntegerField(max_length=4, verbose_name='Year module is taught')),
            ],
        ),
        migrations.CreateModel(
            name='Profs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20, verbose_name="Professor's full name")),
            ],
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(default=5, verbose_name='Proffessor rating')),
                ('modules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate.modules')),
                ('profs', models.ManyToManyField(to='rate.profs')),
            ],
        ),
    ]