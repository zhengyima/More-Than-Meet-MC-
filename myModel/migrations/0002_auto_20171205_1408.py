# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myModel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('lno', models.AutoField(serialize=False, primary_key=True)),
                ('ldetail', models.TextField()),
                ('ltime', models.DateTimeField()),
            ],
            options={
                'db_table': 'logs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MymodelTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'myModel_test',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('ono', models.AutoField(serialize=False, primary_key=True)),
                ('oid', models.CharField(max_length=30)),
                ('bno', models.CharField(max_length=30)),
                ('sno', models.IntegerField()),
                ('bhour', models.IntegerField()),
                ('bneed', models.IntegerField()),
                ('bnote', models.TextField()),
                ('otime', models.DateTimeField()),
                ('ostatus', models.IntegerField()),
                ('osign', models.CharField(max_length=40)),
                ('osign2', models.CharField(max_length=40)),
                ('prepay_id', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'Orders',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('sno', models.AutoField(serialize=False, primary_key=True)),
                ('sname', models.CharField(max_length=10)),
                ('sgender', models.CharField(max_length=1)),
                ('sage', models.IntegerField()),
                ('sheight', models.IntegerField()),
                ('sweight', models.IntegerField()),
                ('sxz', models.CharField(max_length=3)),
                ('sschool', models.CharField(max_length=10)),
                ('smajor', models.CharField(max_length=10)),
                ('sgrade', models.CharField(max_length=10)),
                ('stime', models.CharField(max_length=20)),
                ('srange', models.TextField()),
                ('swage', models.IntegerField()),
                ('sinfo', models.TextField()),
                ('simg', models.ImageField(upload_to='images')),
                ('slike', models.IntegerField()),
                ('scharm', models.IntegerField()),
                ('snum', models.IntegerField()),
            ],
            options={
                'db_table': 'Seller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SellerDisplay',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sno', models.IntegerField()),
                ('sflag', models.IntegerField()),
            ],
            options={
                'db_table': 'Seller_display',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SellerImage',
            fields=[
                ('ino', models.AutoField(serialize=False, primary_key=True)),
                ('iurl', models.ImageField(upload_to='images')),
                ('sno', models.IntegerField()),
            ],
            options={
                'db_table': 'Seller_image',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SellerLabel',
            fields=[
                ('lno', models.AutoField(serialize=False, primary_key=True)),
                ('lname', models.CharField(max_length=5)),
                ('sno', models.IntegerField()),
            ],
            options={
                'db_table': 'Seller_label',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SellerLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bno', models.CharField(max_length=32)),
                ('sno', models.IntegerField()),
            ],
            options={
                'db_table': 'Seller_like',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.CharField(max_length=30, serialize=False, primary_key=True)),
                ('unickname', models.TextField(db_column='unickName')),
                ('ugender', models.IntegerField()),
                ('ulanguage', models.TextField()),
                ('ucity', models.TextField()),
                ('uprovince', models.TextField()),
                ('ucountry', models.TextField()),
                ('uavatarurl', models.TextField()),
                ('usigntime', models.DateTimeField(db_column='USigntime')),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
