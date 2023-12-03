# Generated by Django 4.2.7 on 2023-12-03 06:59

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
            name='Establishment',
            fields=[
                ('est_dbname', models.CharField(blank=True, max_length=100, null=True)),
                ('estid', models.SmallIntegerField(blank=True, null=True)),
                ('estname', models.CharField(blank=True, max_length=100, null=True)),
                ('display', models.CharField(max_length=1)),
                ('est_code', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('ip_details', models.CharField(blank=True, max_length=50, null=True)),
                ('username', models.CharField(blank=True, max_length=150, null=True)),
                ('user_password', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'establishment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IdRoleEst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('establishmentid', models.CharField(max_length=10)),
                ('court_id', models.BigIntegerField(blank=True, null=True)),
                ('user_id', models.SmallIntegerField(blank=True, null=True)),
                ('section_id', models.IntegerField(blank=True, null=True)),
                ('mediation_id', models.IntegerField(blank=True, null=True)),
                ('role_type_id', models.CharField(blank=True, max_length=100, null=True)),
                ('multiple_court_id', models.CharField(blank=True, max_length=255, null=True)),
                ('multiple_section_id', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'id_role_est',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoleMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_type_id', models.IntegerField()),
                ('role_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'role_master',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SessionData',
            fields=[
                ('unixtime', models.IntegerField()),
                ('data', models.TextField(blank=True, null=True)),
                ('id', models.CharField(max_length=40, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'session_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sessions',
            fields=[
                ('session_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('last_activity', models.IntegerField()),
                ('data', models.TextField()),
            ],
            options={
                'db_table': 'sessions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('full_name', models.CharField(blank=True, max_length=150, null=True)),
                ('dt_of_creation', models.DateField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('uid', models.BigIntegerField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=50, null=True)),
                ('sessionuser', models.CharField(blank=True, max_length=100, null=True)),
                ('mycolor', models.SmallIntegerField(blank=True, null=True)),
                ('user_password', models.CharField(blank=True, max_length=100, null=True)),
                ('userid', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('display', models.CharField(max_length=1)),
                ('dashboard_flag', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('court_no', models.CharField(blank=True, max_length=20, null=True)),
                ('establishment_code', models.CharField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'auth_user_profile',
            },
        ),
    ]