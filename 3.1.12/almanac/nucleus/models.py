from django.db import models
from django_mysql.models import JSONField


class NucleusData(models.Model):
    no_param_json = JSONField()
    null_json = JSONField(null=True)
    default_json = JSONField(default=dict)
    null_n_default_json = JSONField(default=dict, null=True)

    no_param_txt = models.TextField()
    null_txt = models.TextField(null=True)
    default_txt = models.TextField(default="")
    null_n_default_txt = models.TextField(default="xyz", null=True)
    null_default_blank_txt = models.TextField(default="abc", null=True, blank=True)
    new_txt = models.TextField(default="abc", null=True, blank=True) 
