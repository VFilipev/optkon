from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название категории")    

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING,null=True, blank=True, verbose_name="Категория")
    description = models.TextField(verbose_name="Описание")
    img = ThumbnailerImageField(upload_to='img/', verbose_name='фото', blank=True, null=True)
    available = models.BooleanField(default=True,blank=True, verbose_name="Доступно на сайте")
    weight = models.FloatField(blank=True, null=True, verbose_name="Вес")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукт"

class Photos(models.Model):    
    product = models.ForeignKey(Product,blank=True,null=True, on_delete = models.DO_NOTHING, related_name='photo_gallery_set')
    img = ThumbnailerImageField(upload_to='img/')

    class Meta:
        verbose_name=u'Фото'
        verbose_name_plural=u'Фото'