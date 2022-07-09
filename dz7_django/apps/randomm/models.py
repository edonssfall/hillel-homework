from django.db import models

class Randomm(Models.models):
    length = models.CharField(max_lenght=100)
    digits = models.BoolenField(default=False)
    specials = models.BoolenField(default=False)
