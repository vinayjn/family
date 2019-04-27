# Generated by Django 2.2 on 2019-04-27 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_auto_20190427_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tree.Member'),
        ),
        migrations.AlterField(
            model_name='member',
            name='picture_url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
