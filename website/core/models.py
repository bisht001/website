from django.db import models
from django.contrib.auth.models import User
# from products.models import 

class headphone(models.Model):
    headphone_image = models.ImageField(upload_to = "core/headphone" ,null=True,blank=True) 
    headphone_name = models.CharField(max_length=200)
    headphone_price = models.IntegerField()
    
    def __str__(self):
        return self.headphone_name
    
    class Meta:
        verbose_name = "headphone"
        verbose_name_plural = "headphones"
    
class watch(models.Model):
    watch_image = models.ImageField(upload_to = "core/watch",null=True,blank=True) 
    watch_name = models.CharField(max_length=200)
    watch_price = models.CharField(max_length=20)
    
    def __str__(self):
        return self.watch_name
    
    class Meta:
        verbose_name = "watch"
        verbose_name_plural = "watches"
        

class rolex_collection(models.Model):
    rolex_image = models.ImageField(upload_to = "core/rolex_collection",null=True,blank=True) 
    rolex_name = models.CharField(max_length=200)
    rolex_price = models.CharField(max_length=20)
    rolex_code = models.CharField(max_length=50, blank=True, null=True,unique=True)
    
    def save(self,*args,**kwargs):
        if not self.pk or not self.rolex_code:
            prefix = 'ROLEX'
            count = rolex_collection.objects.filter().exclude(pk=self.pk).count() + 1
            self.rolex_code = f"{prefix}{count:02d}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.rolex_name
    
    @property
    def brand(self):
        return 'Rolex'
    
    class Meta:
        verbose_name = "rolex_collection"
        verbose_name_plural = "rolex_collection"
        
class hublot_collection(models.Model):
    hublot_image = models.ImageField(upload_to = "core/hublot_collection",null=True,blank=True) 
    hublot_name = models.CharField(max_length=200)
    hublot_price = models.CharField(max_length=20)
    hublot_code = models.CharField(max_length=50, blank=True, null=True,unique=True)
    
    def save(self,*args,**kwargs):
        if not self.pk or not self.hublot_code:
            prefix = 'HUBLOT'
            count = hublot_collection.objects.filter().exclude(pk=self.pk).count() + 1
            self.hublot_code = f"{prefix}{count:02d}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.hublot_name
    
    @property
    def brand(self):
        return 'Hublot'
    
    class Meta:
        verbose_name = "hublot_collection"
        verbose_name_plural = "hublot_collection"
    
    
    
class clothes(models.Model):
    cloth_image_1 = models.ImageField(upload_to="core/cloth/first",null=True,blank=True)
    cloth_image_2 = models.ImageField(upload_to="core/cloth/second",null=True,blank=True)
    cloth_name = models.CharField(max_length=200)
    cloth_price = models.IntegerField()

    def __str__(self):
        return self.cloth_name
    
    class Meta:
        verbose_name = "cloth"
        verbose_name_plural = "clothes"
        
        
# class wishlist(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     product_name = models.CharField(max_length=200)
#     product_desc = models.CharField(max_length=200)
#     product_price = models.CharField(max_length=50)
#     product_Image = models.ImageField(upload_to="core/wishlist",blank=True,null=True)
    
#     def __str__(self):
#         return self.product_name
    
#     class Meta:
#         verbose_name = "Wishlist product"
#         verbose_name_plural = "wishlist product"