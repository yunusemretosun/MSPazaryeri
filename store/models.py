from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class BannerManager(models.Manager):
    def active(self):
        return self.filter(is_active=True)

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', default='images/default.png')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    external_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()
    

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title

class Banner(models.Model):
    baslik = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    resim = models.ImageField(upload_to='images/',default='images/default.png')
    is_active = models.BooleanField(default=True)
    external_url = models.URLField(blank=True, null=True)
    cta_text = models.CharField(max_length=255)
    alt_text = models.CharField(max_length=255)
    objects = models.Manager()
    banners = BannerManager()
    def __str__(self) -> str:
        return self.baslik