from django.db import models

# Create your models here.

class SqlManager (models.Manager):
    def execute_sql(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute ('select first_name, last_name from auth_user a')
            result_list = []
            for row in cursor.fetchall():
                a = self.model(row[0], row[1])
                result_list.append(a)
        return result_list

#class tb_auth_user (models.Model):
#    username = models.CharField(db_column='username')
#    is_staff = models.CharField(db_column='is_staff')
#    objects = SqlManager()
#    class Meta:
#        db_table = 'auth_user'

