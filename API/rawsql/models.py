from django.db import models

# Create your models here.

class rawsql (models.Model):
    id_pk = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=150)
    staff = models.BooleanField()
    objects = models.Manager()

    #class Meta:
    #    abstract = True