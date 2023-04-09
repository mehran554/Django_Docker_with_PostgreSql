from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField


class Product(models.Model):
    title = models.CharField(max_length=200)
    # description = models.TextField()
    description = RichTextField()
    image = models.ImageField(verbose_name=_('Picture image'), upload_to='product/product_cover/', blank=True)
    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    datetime_created = models.DateTimeField(default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class Comment(models.Model):
    PRODUCT_STAR = (
        ('1', _('VeryBad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('VeryGood')),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments')
    # body = models.TextField(verbose_name=_('body'))
    body = RichTextField(verbose_name=_('body'))
    active = models.BooleanField(default=True)
    stars = models.CharField(max_length=10, choices=PRODUCT_STAR, verbose_name=_('stars'))
    datetime_create = models.DateTimeField(_('date_create'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
