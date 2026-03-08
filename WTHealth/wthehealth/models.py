# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Doctor(models.Model):
    nsrno = models.CharField(db_column='NSRNo', primary_key=True, max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=200, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1)  # Field name made lowercase.
    establishment = models.CharField(db_column='Establishment', max_length=1000, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    fieldofpractice = models.CharField(db_column='FieldOfPractice', max_length=5000, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Doctor'


class Hospprocedure(models.Model):
    procedureid = models.CharField(db_column='ProcedureID', primary_key=True, max_length=150, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=500, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=14, decimal_places=2)  # Field name made lowercase.
    patienttype = models.TextField(db_column='PatientType', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    specialtyid = models.ForeignKey('Specialty', models.DO_NOTHING, db_column='SpecialtyID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HospProcedure'


class Hospital(models.Model):
    hospitalname = models.CharField(db_column='HospitalName', primary_key=True, max_length=200, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=500, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    postcode = models.IntegerField(db_column='Postcode')  # Field name made lowercase.
    tel = models.CharField(db_column='Tel', max_length=20, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hospital'


class Hospitaldoctor(models.Model):
    pk = models.CompositePrimaryKey('hospitalname', 'nsrno')
    hospitalname = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='HospitalName')  # Field name made lowercase.
    nsrno = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='NSRNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HospitalDoctor'


class Hospitalspecialty(models.Model):
    pk = models.CompositePrimaryKey('hospitalname', 'specialtyid')
    hospitalname = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='HospitalName')  # Field name made lowercase.
    specialtyid = models.ForeignKey('Specialty', models.DO_NOTHING, db_column='SpecialtyID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HospitalSpecialty'


class Review(models.Model):
    reviewid = models.AutoField(db_column='ReviewID', primary_key=True)  # Field name made lowercase.
    reviewtext = models.CharField(db_column='ReviewText', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating', blank=True, null=True)  # Field name made lowercase.
    reviewdatetime = models.DateField(db_column='ReviewDatetime', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='Author', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hospname = models.CharField(db_column='HospName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    doctor = models.CharField(db_column='Doctor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    specialty = models.CharField(db_column='Specialty', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Review'


class Specialty(models.Model):
    specialtyid = models.CharField(db_column='SpecialtyID', primary_key=True, max_length=50, db_collation='utf8mb3_general_ci')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, db_collation='utf8mb3_general_ci')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Specialty'
