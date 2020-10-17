from django.db import models

# Create your models here.

class SqlManager (models.Manager):
    def __init__(self, name):
        self.name = name
        self.fn_params = []

    def execute_fn(self, fn_params):
        self.fn_params.append(fn_params)
        from django.db import connection
        with connection.cursor() as cursor:
            cursor.execute ("select * from fn_get_staff(%s) a",self.fn_params)
            self.fn_params.clear()
            result_list = []
            for row in cursor.fetchall():
                a = self.model(row[0], row[1])
                result_list.append(a)
        return result_list
        

class abs_tb_auth_user (models.Model):
    username = models.CharField(max_length=150)
    is_staff = models.BooleanField()
    base_man = models.Manager()
    objects = SqlManager('test')
    #class Meta:
    #    abstract = True

