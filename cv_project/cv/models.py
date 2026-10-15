from django.db import models


class Profil(models.Model):
    nama = models.CharField(max_length=100)
    profesi = models.CharField(max_length=100)
    email = models.EmailField()
    tentang = models.TextField()


class Keahlian(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    nama = models.CharField(max_length=50)
