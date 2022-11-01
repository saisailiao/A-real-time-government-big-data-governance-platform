from django.db import models
class User(models.Model):
    username = models.CharField(unique=True, max_length=30)
    userpwd = models.CharField(max_length=30)

    def __str__(self):
        return self.username

class Invite_code(models.Model):
    invite_code = models.CharField(unique=True,max_length=30)

    def __str__(self):
        return self.invite_code