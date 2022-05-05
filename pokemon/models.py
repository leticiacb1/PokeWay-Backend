from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=15)
    
    def __str__(self):
        return '%s - senha : %s' % (self.name, self.password)