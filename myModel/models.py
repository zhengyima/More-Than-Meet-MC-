# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals
#import Image
from django.db import models
'''
class Article(models.Model):
    title = models.CharField('title', max_length=256)
    content = models.TextField('content')
    ph = models.ImageField('image',upload_to='uploadImages')

    pub_date = models.DateTimeField('time1', auto_now_add=True, editable = True)
    update_time = models.DateTimeField('time2',auto_now=True, null=True)
'''
class Orders(models.Model):
    ono = models.AutoField(primary_key=True)
    oid = models.CharField(max_length=30)
    bno = models.CharField(max_length=30)
    sno = models.IntegerField()
    bhour = models.IntegerField()
    bneed = models.IntegerField()
    bnote = models.TextField()
    otime = models.DateTimeField()
    ostatus = models.IntegerField()
    osign = models.CharField(max_length=40)
    osign2 = models.CharField(max_length=40)
    prepay_id = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'Orders'


class Seller(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=10)
    sgender = models.CharField(max_length=1)
    sage = models.IntegerField()
    sheight = models.IntegerField()
    sweight = models.IntegerField()
    sxz = models.CharField(max_length=3)
    sschool = models.CharField(max_length=10)
    smajor = models.CharField(max_length=10)
    sgrade = models.CharField(max_length=10)
    stime = models.CharField(max_length=20)
    srange = models.TextField()
    swage = models.IntegerField()
    sinfo = models.TextField()
   # simg = models.TextField()
    simg = models.ImageField(upload_to='images')
    slike = models.IntegerField()
    scharm = models.IntegerField()
    snum = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Seller'


class SellerDisplay(models.Model):
    sno = models.IntegerField(primary_key=True)
    sflag = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Seller_display'


class SellerImage(models.Model):
    ino = models.AutoField(primary_key=True)
    iurl = models.ImageField(upload_to='images')
#    iurl = models.ImageField(upload_to='images')
    sno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Seller_image'


class SellerLabel(models.Model):
    lno = models.AutoField(primary_key=True)
    lname = models.CharField(max_length=5)
    sno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Seller_label'


class SellerLike(models.Model):
    bno = models.CharField(max_length=32,primary_key=True)
    sno = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Seller_like'
        unique_together = (('bno', 'sno'),)


class Users(models.Model):
    uid = models.CharField(primary_key=True, max_length=30)
    unickname = models.TextField(db_column='unickName')  # Field name made lowercase.
    ugender = models.IntegerField()
    ulanguage = models.TextField()
    ucity = models.TextField()
    uprovince = models.TextField()
    ucountry = models.TextField()
    uavatarurl = models.TextField()
    usigntime = models.DateTimeField(db_column='USigntime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Logs(models.Model):
    lno = models.AutoField(primary_key=True)
    ldetail = models.TextField()
    ltime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'logs'


class MymodelTest(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'myModel_test'
