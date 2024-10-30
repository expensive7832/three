# Generated by Django 5.1.2 on 2024-10-30 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=14)),
                ('mobile_network', models.CharField(choices=[('mtn', 'MTN'), ('airtel', 'AIRTEL'), ('9mobile', '(9MOBILE)'), ('glo', 'GLO')], max_length=10)),
                ('message', models.CharField(max_length=200)),
                ('ref_code', models.CharField(max_length=100, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
