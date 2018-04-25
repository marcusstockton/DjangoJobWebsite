# Generated by Django 2.0.4 on 2018-04-19 15:04

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Address', '0002_auto_20170110_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Address.AddressType'),
        ),
    ]