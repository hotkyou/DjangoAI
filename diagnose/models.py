# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Answer(models.Model):
    answerpk = models.AutoField(primary_key=True)
    listpk = models.ForeignKey('List', models.DO_NOTHING, db_column='listpk')
    answer = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'answer'


class Checkans(models.Model):
    checkanspk = models.AutoField(primary_key=True)
    listpk = models.ForeignKey('List', models.DO_NOTHING, db_column='listpk')
    answerpk = models.ForeignKey(Answer, models.DO_NOTHING, db_column='answerpk')

    class Meta:
        managed = False
        db_table = 'checkans'


class Checklist(models.Model):
    checklistpk = models.AutoField(primary_key=True)
    sessionpk = models.ForeignKey('Session', models.DO_NOTHING, db_column='sessionpk')
    checkanspk = models.ForeignKey(Checkans, models.DO_NOTHING, db_column='checkanspk')

    class Meta:
        managed = False
        db_table = 'checklist'


class Format(models.Model):
    formatpk = models.AutoField(primary_key=True)
    format = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'format'


class List(models.Model):
    listpk = models.AutoField(primary_key=True)
    versionpk = models.ForeignKey('Version', models.DO_NOTHING, db_column='versionpk')
    formatpk = models.ForeignKey(Format, models.DO_NOTHING, db_column='formatpk')
    question = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'list'


class Session(models.Model):
    sessionpk = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=255)
    sitepk = models.ForeignKey('Site', models.DO_NOTHING, db_column='sitepk')
    snow = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'session'


class Site(models.Model):
    sitepk = models.AutoField(primary_key=True)
    site = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'site'


class Version(models.Model):
    versionpk = models.AutoField(primary_key=True)
    vnow = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'version'
