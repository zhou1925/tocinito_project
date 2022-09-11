import redis
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import OrderItem

r = redis.Redis(host='localhost',port=6379, db=0, charset="utf-8", decode_responses=True)

@receiver(post_save, sender=OrderItem)
def save_profile(sender, instance, created, **kwargs):
    """ OrderItem """
    order_item = instance
    if created:
        try:
            slug = order_item.product.slug
            r.zincrby("products", 1, slug)
        except:
            pass
