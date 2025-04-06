from django.db import models
from django.core.exceptions import ValidationError


TYPE_CHOICES = [
    ("Platinum", "Platinum"),
    ("Gold", "Gold"),
    ("Silver", "Silver"),
    ("Diamond", "Diamond"),
]

class CategoryModel(models.Model):
    type = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.type}"
    
    class Meta:
        verbose_name = "Available Categories"
        verbose_name_plural = "Categories"


class ProductModel(models.Model):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    weight = models.CharField(max_length=50, null=True, blank=True)
    price = models.IntegerField()
    show_order = models.IntegerField(default=10)
    
    img1 = models.ImageField(upload_to="images", max_length=None, verbose_name="Image")
    img2 = models.ImageField(upload_to="images", max_length=None, null=True, blank=True, verbose_name="Image 2 (optional)")
    img3 = models.ImageField(upload_to="images", max_length=None, null=True, blank=True, verbose_name="Image 3 (optional)")
    img4 = models.ImageField(upload_to="images", max_length=None, null=True, blank=True, verbose_name="Image 4 (optional)")
    img5 = models.ImageField(upload_to="images", max_length=None, null=True, blank=True, verbose_name="Image 5 (optional)")
    
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    
    class Meta:
        verbose_name = "Available Products"
        verbose_name_plural = "Products"
        ordering = ["show_order"]

    def __str__(self):
        return f"{self.name} - {self.type}"


class BannerModel(models.Model):
    img1 = models.ImageField(upload_to="banner", max_length=None, verbose_name="Image")
    img2 = models.ImageField(upload_to="banner", max_length=None, null=True, blank=True, verbose_name="Image 2 (optional)")
    img3 = models.ImageField(upload_to="banner", max_length=None, null=True, blank=True, verbose_name="Image 3 (optional)")
    img4 = models.ImageField(upload_to="banner", max_length=None, null=True, blank=True, verbose_name="Image 4 (optional)")
    img5 = models.ImageField(upload_to="banner", max_length=None, null=True, blank=True, verbose_name="Image 5 (optional)")

    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banner"
        
    def save(self, *args, **kwargs):
        if BannerModel.objects.exists() and not self.pk:
            raise ValidationError("Banner already exists, try after removing it.")
        super().save(*args, **kwargs)
        
    def __str__(self):
        return "Click to edit banner images"
        

class GoldPrice(models.Model):
    gold_1g = models.CharField(max_length=15, verbose_name="1gm gold price")
    gold_8g = models.CharField(max_length=15, verbose_name="8gm gold price")
    silver_1g = models.CharField(max_length=15, verbose_name="1gm silver price")
    
    class Meta:
        verbose_name = "Price Manager"
        verbose_name_plural = "Price list"
        
    def save(self, *args, **kwargs):
        if GoldPrice.objects.exists() and not self.pk:
            raise ValidationError("Price manager already exists, try after removing it.")
        super().save(*args, **kwargs)
        
    def __str__(self):
        return "Click to update today price"