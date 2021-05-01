# Generated by Django 3.2 on 2021-04-27 10:33

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email_address')),
                ('phone', models.IntegerField()),
                ('profilepic', models.ImageField(upload_to='profile/')),
                ('address', models.CharField(max_length=250)),
                ('client', models.BooleanField(default=False)),
                ('casier', models.BooleanField(default=False)),
                ('manager', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
