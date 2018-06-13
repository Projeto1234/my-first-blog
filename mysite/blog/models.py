from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Musico(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    origem = models.TextField()

    def __str__(self):
        return self.first_name+" "+self.last_name

class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    id_musico = models.ForeignKey(Musico)
    nome = models.TextField()
    data_lancamento = models.DateField()
    avaliacao = models.FloatField()
    def __str__(self):
        return self.nome

class Musica(models.Model):

    id = models.IntegerField(primary_key=True)
    id_album = models.ForeignKey(Album)
    nome = models.TextField()
    data = models.DateField()
    genero = models.TextField()
    avaliacao = models.FloatField()
