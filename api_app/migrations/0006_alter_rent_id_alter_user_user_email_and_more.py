# Generated by Django 4.1 on 2022-08-16 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0005_alter_user_user_email_alter_user_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='id',
            field=models.AutoField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_password',
            field=models.CharField(max_length=200),
        ),
    ]