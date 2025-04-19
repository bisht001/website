from django.db import models

# Create your models here.

def image_upload_path(instance,filename):
    if instance.watch_brand:
        brand_name = instance.watch_brand
    else:
        brand_name = 'other'
    return f"product/{brand_name}/watch/{filename}"
      
class watch_collection(models.Model):
    
    watch_image_1 = models.ImageField(upload_to = image_upload_path,null=True,blank=True)
    watch_name = models.CharField(max_length=50)
    watch_desc = models.TextField(default="Best watch")
    watch_full_name = models.CharField(max_length=100)
    watch_model_case = models.CharField(max_length=50)
    watch_material = models.CharField(max_length=50)
    watch_price = models.CharField(max_length=30)
    watch_reference_no  = models.CharField(max_length=50)
    watch_brand = models.CharField(max_length=50,choices=[
        ('Rolex','Rolex'),
        ('Hublot','Hublot')
    ])
    watch_code = models.CharField(max_length=50, blank=True, null=True,unique=True)
    
    def save(self,*args,**kwargs):
        if not self.pk or not self.watch_code:
            prefix = self.watch_brand.upper()
            count = watch_collection.objects.filter(watch_brand =self.watch_brand).exclude(pk=self.pk).count() + 1
            self.watch_code = f"{prefix}{count:02d}"
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.watch_name
    
    class Meta:
        verbose_name = "Watch_product"
        verbose_name_plural = "Watch_list"
     