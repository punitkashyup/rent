# Generated by Django 4.1 on 2022-08-19 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateField(auto_now_add=True)),
                ('rentmonth', models.CharField(max_length=30)),
                ('rent_amount', models.FloatField()),
                ('bijli_bill', models.FloatField()),
                ('other_amount', models.FloatField(blank=True)),
                ('other_commnet', models.CharField(blank=True, max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
