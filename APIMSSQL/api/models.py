from django.db import models

# Create your models here.

class SqlManager (models.Manager):
    def execute_sql(self):
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute ('select username, is_staff from auth_user a')
            result_list = []
            for row in cursor.fetchall():
                a = self.model(row[0], row[1])
                result_list.append(a)
            return cursor.fetchall()

class api_auth_user (models.Model):
    #id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    #objects = models.Manager()
    objects = SqlManager()