# Generated by Django 4.0.6 on 2023-02-17 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={},
        ),
        migrations.RemoveField(
            model_name='project',
            name='finish_date',
        ),
        migrations.RemoveField(
            model_name='project',
            name='starting_date',
        ),
        migrations.CreateModel(
            name='Student_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.DateField()),
                ('finish_date', models.DateField(null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.project')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.student')),
            ],
        ),
    ]