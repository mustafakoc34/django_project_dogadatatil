from django.db import models


# Create your models here.

class Karavanlar(models.Model):
    title = models.CharField(("Karavan Modeli"), max_length=200)
    description = models.TextField(("Karavan Detayı"), max_length=200)
    image = models.FileField(("Model Resmi"), upload_to='', max_length=100, null=True)
    

    class Meta:
        verbose_name_plural ="Karavan"
    

    def __str__(self):
        return self.title

class Bungalov(models.Model):
    title = models.CharField(("Bungalov Modeli"), max_length=200)
    description = models.TextField(("Bungalov Detayı"), max_length=200)
    image = models.FileField(("Model Resmi"), upload_to='', max_length=100, null=True)
    

    class Meta:
        verbose_name_plural ="Bungalov"

    def __str__(self):
        return self.title

class Tent(models.Model):
    title = models.CharField(("Çadır Modeli"), max_length=50)
    description = models.TextField(("Çadır Hakkında Detaylar"), max_length=200)
    image = models.FileField(("Çadır Resmi"), upload_to='', max_length=100, null=True)
    

    class Meta:
        verbose_name_plural ="Çadır"

    def __str__(self):
        return self.title

class Comment(models.Model):
    karavan_category = models.ForeignKey(Karavanlar, verbose_name=("Karavan Modelleri"), blank=True, null=True, on_delete=models.CASCADE)
    bungalov_category = models.ForeignKey(Bungalov, verbose_name=("Bungalov Modelleri"), blank=True, null=True, on_delete=models.CASCADE)
    tent_category = models.ForeignKey(Tent, verbose_name=("Çadır Modelleri"), blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(("Yorum Yapan Kişi"), max_length=50)
    title = models.CharField(("Yorum Başlığı"), max_length=50)
    text = models.TextField(("Yorum"), max_length=200)
    date_now = models.DateTimeField(("yorum yapılma zamanı"), auto_now_add=True)

