# Generated by Django 2.1.4 on 2018-12-24 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0005_auto_20181221_1051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='applicant_cv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Attachment.Attachment'),
        ),
    ]
