# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class EtimRawDataNew(models.Model):
    depot_cd = models.CharField(max_length=10, blank=True, null=True)
    dutydate = models.DateField(db_column='dutyDate')  # Field name made lowercase.
    waybilldate = models.DateTimeField(db_column='waybillDate')  # Field name made lowercase.
    waybillcollectiondate = models.DateField(db_column='waybillCollectionDate')  # Field name made lowercase.
    ticketid = models.IntegerField(primary_key=True,db_column='ticketId')  # Field name made lowercase.
    full_amt = models.FloatField(db_column='FULL_AMT', blank=True, null=True)  # Field name made lowercase.
    full_pax = models.IntegerField(db_column='FULL_PAX')  # Field name made lowercase.
    routeno = models.CharField(db_column='routeNo', max_length=6)  # Field name made lowercase.
    empcode = models.CharField(db_column='empCode', max_length=10)  # Field name made lowercase.
    ticket_bus_no = models.CharField(db_column='TICKET_BUS_NO', max_length=10)  # Field name made lowercase.
    ttl_tkt_issue = models.FloatField(db_column='TTL_TKT_ISSUE', blank=True, null=True)  # Field name made lowercase.
    etimticketcodeid = models.IntegerField(db_column='etimTicketCodeId')  # Field name made lowercase.
    ticketcode = models.CharField(db_column='ticketCode', max_length=2)  # Field name made lowercase.
    rupee_deno = models.FloatField(db_column='RUPEE_DENO', blank=True, null=True)  # Field name made lowercase.
    full_tkt = models.CharField(db_column='FULL_TKT', max_length=1)  # Field name made lowercase.
    bottkt = models.BigIntegerField()
    machineno = models.CharField(db_column='machineNo', max_length=8)  # Field name made lowercase.
    ticketdate = models.CharField(db_column='ticketDate', max_length=8)  # Field name made lowercase.
    tickettime = models.CharField(db_column='ticketTime', max_length=8)  # Field name made lowercase.
    fromstopcode = models.CharField(db_column='fromStopcode', max_length=11)  # Field name made lowercase.
    frmstopname = models.CharField(db_column='frmStopName', max_length=30)  # Field name made lowercase.
    tostopname = models.CharField(db_column='toStopname', max_length=30)  # Field name made lowercase.
    tostopcode = models.CharField(db_column='toStopCode', max_length=11)  # Field name made lowercase.
    fromstageno = models.CharField(db_column='fromStageNo', max_length=3)  # Field name made lowercase.
    tostageno = models.CharField(db_column='toStageNo', max_length=3)  # Field name made lowercase.
    hexwaybillno = models.CharField(db_column='hexwaybillNo', max_length=12)  # Field name made lowercase.
    tripno = models.IntegerField(db_column='tripNo')  # Field name made lowercase.
    tripdirection = models.CharField(db_column='tripDirection', max_length=1)  # Field name made lowercase.
    docketno = models.CharField(db_column='docketNo', max_length=17)  # Field name made lowercase.
    concessionid = models.IntegerField(db_column='concessionId')  # Field name made lowercase.
    serialno = models.IntegerField(db_column='serialNo')  # Field name made lowercase.
    ep_flag = models.CharField(max_length=7)
    sent_flag = models.CharField(max_length=1)
    inserteddate = models.DateTimeField(db_column='insertedDate')  # Field name made lowercase.
    modifieddate = models.DateTimeField(db_column='modifiedDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'etim_raw_data_new'
