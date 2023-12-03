from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model


class Establishment(models.Model):
    est_dbname = models.CharField(max_length=100, blank=True, null=True)
    estid = models.SmallIntegerField(blank=True, null=True)
    estname = models.CharField(max_length=100, blank=True, null=True)
    display = models.CharField(max_length=1)
    est_code = models.CharField(primary_key=True, max_length=10)
    ip_details = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True)
    user_password = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'establishment'


class IdRoleEst(models.Model):
    establishmentid = models.CharField(max_length=10)
    court_id = models.BigIntegerField(blank=True, null=True)
    user_id = models.SmallIntegerField(blank=True, null=True)
    section_id = models.IntegerField(blank=True, null=True)
    mediation_id = models.IntegerField(blank=True, null=True)
    role_type_id = models.CharField(max_length=100, blank=True, null=True)
    multiple_court_id = models.CharField(max_length=255, blank=True, null=True)
    multiple_section_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'id_role_est'


class RoleMaster(models.Model):
    role_type_id = models.IntegerField()
    role_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role_master'


class SessionData(models.Model):
    unixtime = models.IntegerField()
    data = models.TextField(blank=True, null=True)
    id = models.CharField(primary_key=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'session_data'


class Sessions(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40)
    last_activity = models.IntegerField()
    data = models.TextField()

    class Meta:
        managed = False
        db_table = 'sessions'


class Users(models.Model):
    username = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(blank=True, null=True, max_length=100)
    full_name = models.CharField(max_length=150, blank=True, null=True)
    dt_of_creation = models.DateField(blank=True, null=True)
    email = models.CharField(blank=True, null=True, max_length=100)
    uid = models.BigIntegerField(blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    sessionuser = models.CharField(max_length=100, blank=True, null=True)
    mycolor = models.SmallIntegerField(blank=True, null=True)
    user_password = models.CharField(max_length=100, blank=True, null=True)
    userid = models.SmallIntegerField(primary_key=True)
    display = models.CharField(max_length=1)
    dashboard_flag = models.CharField(blank=True, null=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'users'



def get_username(self):
    return self.first_name+' '+self.last_name

User.add_to_class("__str__", get_username)

class Profile(models.Model):

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
        db_table = 'auth_user_profile'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    court_no = models.CharField(max_length=20, null=True, blank=True)
    establishment_code = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()