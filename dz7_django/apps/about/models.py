from django.db import models

class Whoami(models.Model):
    user_agent = models.CharField(max_length=255)
    ip_adress = models.CharField(max_length=16)
    now_time = models.CharField(max_length=255)