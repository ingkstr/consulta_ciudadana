# Generated by Django 2.2.9 on 2020-01-06 17:40

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=250)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField()),
                ('question0', models.TextField()),
                ('question1', models.TextField(blank=True, null=True)),
                ('question2', models.TextField(blank=True, null=True)),
                ('question3', models.TextField(blank=True, null=True)),
                ('question4', models.TextField(blank=True, null=True)),
                ('question5', models.TextField(blank=True, null=True)),
                ('question6', models.TextField(blank=True, null=True)),
                ('question7', models.TextField(blank=True, null=True)),
                ('question8', models.TextField(blank=True, null=True)),
                ('question9', models.TextField(blank=True, null=True)),
                ('ready', models.BooleanField(default=False)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('modificated_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('cid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('born_date', models.DateField()),
                ('alive', models.BooleanField()),
                ('registered_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, help_text='Set to true if he is staff', verbose_name='He is staff')),
                ('is_voting_chief', models.BooleanField(default=True, help_text='Set to true when the user is voting chief', verbose_name='He is voting chief')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
