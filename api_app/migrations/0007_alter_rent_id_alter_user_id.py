# Generated by Django 4.1 on 2022-08-16 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0006_alter_rent_id_alter_user_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
