from django.db import models


# Create your models here.

class Karavanlar(models.Model):
    karavanModeli = models.CharField(("Karavan Modeli"), max_length=200)
    aciklama = models.TextField(("Karavan Detayı"), max_length=200)
    image = models.FileField(("Model Resmi"), upload_to='', max_length=100, null=True)
    

    def __str__(self):
        return self.karavanModeli

class Bungalov(models.Model):
    bungalovModeli = models.CharField(("Bungalov Modeli"), max_length=200)
    aciklama = models.TextField(("Bungalov Detayı"), max_length=200)
    image = models.FileField(("Model Resmi"), upload_to='', max_length=100, null=True)

    def __str__(self):
        return self.bungalovModeli

class Tent(models.Model):
    cadirModeli = models.CharField(("Çadır Modeli"), max_length=50)
    aciklama = models.TextField(("Çadır Hakkında Detaylar"), max_length=200)
    image = models.FileField(("Çadır Resmi"), upload_to='', max_length=100, null=True)

    def __str__(self):
        return self.cadirModeli

class Comment(models.Model):
    karavan_category = models.ForeignKey(Karavanlar, verbose_name=("Karavan Modelleri"), blank=True, null=True, on_delete=models.CASCADE)
    bungalov_category = models.ForeignKey(Bungalov, verbose_name=("Bungalov Modelleri"), blank=True, null=True, on_delete=models.CASCADE)
    tent_category = models.ForeignKey(Tent, verbose_name=("Çadır Modelleri"), blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(("Yorum Yapan Kişi"), max_length=50)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"), max_length=200)
    date_now = models.DateTimeField(("yorum yapılma zamanı"), auto_now_add=True)

