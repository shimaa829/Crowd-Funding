# Generated by Django 2.1.5 on 2020-03-27 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('projects', '0004_auto_20200324_2316'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.Profile'),
            preserve_default=False,
        ),
    ]
