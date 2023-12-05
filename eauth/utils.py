from django.db import connections
from eauth.models import Establishment, Users


def get_establishment(establishment):
    # with connections['ecourtisuserdb'].cursor() as cursor:
    #     cursor.execute("select est_code from establishment where est_dbname= %s ", [establishment])
    #     return cursor.fetchone()
    data = Establishment.objects.using('ecourtisuserdb').filter(est_dbname=establishment).first()
    return data.est_code


def verify_user_role(user, establishment):
    with connections['ecourtisuserdb'].cursor() as cursor:
        cursor.execute("select establishmentid, user_id, court_id from id_role_est where user_id= %s and establishmentid= %s and court_id is not null", [user, establishment])
        result = cursor.fetchone()
        return result
    
    
def get_user(username):
    return Users.objects.using('ecourtisuserdb').filter(username=username).first()
