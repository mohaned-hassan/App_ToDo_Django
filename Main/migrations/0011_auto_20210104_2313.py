# Generated by Django 3.0.8 on 2021-01-04 23:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0010_auto_20210104_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='CustomList',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Main.CustomList'),
        ),
    ]