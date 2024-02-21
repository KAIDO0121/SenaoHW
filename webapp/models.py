from django.db import models


# should only interact with database in this layer, for scaling purpose i overwrite the create function
class UserManager(models.Manager):
    def create(self, **obj_data):
        return super().create(**obj_data)

class User(models.Model):


    username = models.CharField("UserName", unique = True, blank = False)
    password = models.CharField("Password", blank = False)

    def __str__(self):
        return self.username
