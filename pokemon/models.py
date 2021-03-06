from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200, primary_key=True)
    password = models.CharField(max_length=15)
    selectedFirtsPokemon = models.BooleanField(default=False)
    
    def __str__(self):
        return '%s' % (self.name)

class Pokemon(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    move1 = models.CharField(max_length=100)
    move2 = models.CharField(max_length=100)
    move3 = models.CharField(max_length=100)
    favorite = models.BooleanField(default=False)

    srcImg = models.CharField(max_length=300)
    srcImgBack = models.CharField(max_length=300)

    hp = models.CharField(max_length=100)
    level = models.CharField(max_length=100)

    def __str__(self):
        return '%s - idUser : %s' % (self.id, self.idUser)
