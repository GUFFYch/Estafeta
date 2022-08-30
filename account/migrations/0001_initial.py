# Generated by Django 4.0.4 on 2022-08-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(default='', max_length=254, unique=True)),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('phone', models.IntegerField(default='1')),
                ('city', models.CharField(default='', max_length=30)),
                ('userImage', models.ImageField(default='images/default.png', upload_to='images/')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('name_small', models.CharField(default='', max_length=20)),
                ('nameFull', models.CharField(default='', max_length=20)),
                ('payment_account', models.IntegerField(default=0)),
                ('reg_form', models.CharField(default='', max_length=20)),
                ('inn', models.IntegerField(default=0)),
                ('ogrn', models.IntegerField(default=0)),
                ('korr_check', models.IntegerField(default=0)),
                ('kpp', models.IntegerField(default=0)),
                ('index', models.IntegerField(default=0)),
                ('bik', models.IntegerField(default=0)),
                ('checking_account', models.IntegerField(default=0)),
                ('fiz_adress', models.CharField(default='', max_length=9999)),
                ('street', models.CharField(default='', max_length=9999)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
