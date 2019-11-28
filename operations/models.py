# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chapitre(models.Model):
    chap = models.CharField(db_column='CHAP', max_length=3, blank=True, primary_key=True)  # Field name made lowercase.
    sect = models.SmallIntegerField(db_column='SECT', blank=True, null=True)  # Field name made lowercase.
    ssect = models.SmallIntegerField(db_column='SSECT', blank=True, null=True)  # Field name made lowercase.
    libchap = models.CharField(db_column='LIBCHAP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    libsect = models.CharField(db_column='LIBSECT', max_length=30, blank=True, null=True)  # Field name made lowercase.
    libssect = models.CharField(db_column='LIBSSECT', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Chapitre'


class Commune(models.Model):
    gest = models.CharField(db_column='GEST', max_length=7, blank=True, primary_key=True)  # Field name made lowercase.
    libgest = models.CharField(db_column='LIBGEST', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ndaira = models.SmallIntegerField(db_column='NDAIRA', blank=True, null=True)  # Field name made lowercase.
    daira = models.CharField(db_column='DAIRA', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Commune'


class Consommation(models.Model):
    nop = models.CharField(db_column='NOP', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    datecons = models.DateTimeField(db_column='DATECONS', blank=True, null=True)  # Field name made lowercase.
    cons = models.FloatField(db_column='CONS', blank=True, null=True)  # Field name made lowercase.
    remise = models.SmallIntegerField(db_column='REMISE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Consommation'


class Consommation2017Remise03(models.Model):
    nop = models.CharField(db_column='NOP', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    datecons = models.DateTimeField(db_column='DATECONS', blank=True, null=True)  # Field name made lowercase.
    cons = models.FloatField(db_column='CONS', blank=True, null=True)  # Field name made lowercase.
    remise = models.SmallIntegerField(db_column='REMISE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Consommation2017 REMISE 03'


class Consommationarchive(models.Model):
    nop = models.CharField(db_column='NOP', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    datecons = models.DateTimeField(db_column='DATECONS', blank=True, null=True)  # Field name made lowercase.
    cons = models.FloatField(db_column='CONS', blank=True, null=True)  # Field name made lowercase.
    remise = models.SmallIntegerField(db_column='REMISE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ConsommationArchive'


class CopieDeOprationRemise6(models.Model):
    nop = models.CharField(db_column='NOP', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    chap = models.CharField(db_column='CHAP', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gest = models.CharField(db_column='GEST', max_length=7, blank=True, null=True)  # Field name made lowercase.
    anins = models.CharField(db_column='ANINS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    decap = models.CharField(db_column='DECAP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ndins = models.CharField(db_column='NDINS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    apinit = models.FloatField(db_column='APINIT', blank=True, null=True)  # Field name made lowercase.
    apact = models.FloatField(db_column='APACT', blank=True, null=True)  # Field name made lowercase.
    sitop = models.CharField(db_column='SITOP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    datelanc = models.DateTimeField(db_column='DATELANC', blank=True, null=True)  # Field name made lowercase.
    consant = models.FloatField(db_column='CONSANT', blank=True, null=True)  # Field name made lowercase.
    consenc = models.FloatField(db_column='CONSENC', blank=True, null=True)  # Field name made lowercase.
    pop = models.IntegerField(db_column='POP', blank=True, null=True)  # Field name made lowercase.
    emplp = models.SmallIntegerField(db_column='EmplP', blank=True, null=True)  # Field name made lowercase.
    emplt = models.SmallIntegerField(db_column='EmplT', blank=True, null=True)  # Field name made lowercase.
    physique = models.CharField(db_column='Physique', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taux = models.SmallIntegerField(db_column='Taux', blank=True, null=True)  # Field name made lowercase.
    prog = models.CharField(db_column='Prog', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dateclot = models.DateTimeField(db_column='DATECLOT', blank=True, null=True)  # Field name made lowercase.
    ndclot = models.CharField(db_column='NDCLOT', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nfixe = models.SmallIntegerField(db_column='NFIXE', blank=True, null=True)  # Field name made lowercase.
    numfixe = models.CharField(db_column='NumFIXE', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Copie de Op�ration remise 6'


class Exercice(models.Model):
    exercice = models.SmallIntegerField(db_column='Exercice', blank=True, primary_key=True)  # Field name made lowercase.
    cloture = models.BooleanField(db_column='Cloture', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Exercice'


class Mouvement(models.Model):
    nop = models.CharField(db_column='NOP', max_length=25, blank=True, primary_key=True)  # Field name made lowercase.
    datm = models.DateTimeField(db_column='DATM', blank=True, null=True)  # Field name made lowercase.
    ndm = models.CharField(db_column='NDM', max_length=3, blank=True, null=True)  # Field name made lowercase.
    typem = models.CharField(db_column='TYPEM', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mini = models.FloatField(db_column='MINI', blank=True, null=True)  # Field name made lowercase.
    mfin = models.FloatField(db_column='MFIN', blank=True, null=True)  # Field name made lowercase.
    numfixe = models.CharField(db_column='NumFIXE', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mouvement'


class Operation(models.Model):
    nop = models.CharField(db_column='NOP', primary_key=True, max_length=25)  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=250, blank=True, null=True)  # Field name made lowercase.
    chap = models.CharField(db_column='CHAP', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gest = models.CharField(db_column='GEST', max_length=7, blank=True, null=True)  # Field name made lowercase.
    anins = models.CharField(db_column='ANINS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    decap = models.CharField(db_column='DECAP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ndins = models.CharField(db_column='NDINS', max_length=3, blank=True, null=True)  # Field name made lowercase.
    apinit = models.FloatField(db_column='APINIT', blank=True, null=True)  # Field name made lowercase.
    apact = models.FloatField(db_column='APACT', blank=True, null=True)  # Field name made lowercase.
    sitop = models.CharField(db_column='SITOP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    datelanc = models.DateTimeField(db_column='DATELANC', blank=True, null=True)  # Field name made lowercase.
    consant = models.FloatField(db_column='CONSANT', blank=True, null=True)  # Field name made lowercase.
    consenc = models.FloatField(db_column='CONSENC', blank=True, null=True)  # Field name made lowercase.
    pop = models.IntegerField(db_column='POP', blank=True, null=True)  # Field name made lowercase.
    emplp = models.SmallIntegerField(db_column='EmplP', blank=True, null=True)  # Field name made lowercase.
    emplt = models.SmallIntegerField(db_column='EmplT', blank=True, null=True)  # Field name made lowercase.
    physique = models.CharField(db_column='Physique', max_length=255, blank=True, null=True)  # Field name made lowercase.
    taux = models.SmallIntegerField(db_column='Taux', blank=True, null=True)  # Field name made lowercase.
    prog = models.CharField(db_column='Prog', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dateclot = models.DateTimeField(db_column='DATECLOT', blank=True, null=True)  # Field name made lowercase.
    ndclot = models.CharField(db_column='NDCLOT', max_length=6, blank=True, null=True)  # Field name made lowercase.
    nfixe = models.SmallIntegerField(db_column='NFIXE', blank=True, null=True)  # Field name made lowercase.
    numfixe = models.CharField(db_column='NumFIXE', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Operation'


class Outils(models.Model):
    mdp = models.CharField(db_column='MDP', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Outils'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
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
    action_flag = models.SmallIntegerField()
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
