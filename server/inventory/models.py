from django.db import models
from datetime import timedelta
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save

class Provider(models.Model):
    name = models.CharField(max_length=150)
    phone = models.CharField(max_length=12, unique=True)
    address = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Provedor'
        verbose_name_plural = 'Provedores'

    def __str__(self):
        return self.name

class Product(models.Model):
    STATUS_GOOD = 'GOOD'
    STATUS_CRITICAL = 'CRITICAL'

    name = models.CharField(max_length=40)
    quantity = models.PositiveIntegerField(default=0)
    min = models.PositiveIntegerField(default=0)
    desired = models.PositiveIntegerField(default=0)
    max = models.PositiveIntegerField(default=0)
    expire_date = models.DateField(default=timezone.now, blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.name
    
    def days_left(self):
        today = timezone.now().date()
        day_left = self.expire_date - today
        return day_left
    
    def status(self):
        """ return status of a product """
        DAYS_20 = timedelta(days=20)
        DAYS_10 = timedelta(days=10)
        DAYS_0 = timedelta(days=0)

        time_left = self.days_left()
        
        if time_left > DAYS_20:
            return "GOOD"
        elif time_left < DAYS_20 and time_left > DAYS_0:
            return "CRITICAL"
        elif time_left < DAYS_0:
            return "EXPIRED"

    def buy_suggestion(self):
        qty_to_buy = 0

        if self.quantity >= self.min and self.quantity <= self.desired:
            qty_to_buy = self.desired - self.quantity
        elif self.quantity < self.min:
            qty_to_buy = self.desired - self.quantity
        elif self.quantity > self.max:
            return f"overcharge by {self.quantity - self.max}"
        
        return f"buy x{qty_to_buy}"
        
    
class Transfer(models.Model):                                   
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Transferencia'
        verbose_name_plural = 'Transferencias'
    
    def __str__(self):
        return str(self.id)
                                     
class TransferItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='item')
    transfer = models.ForeignKey(Transfer, on_delete=models.CASCADE, related_name='transfer_items')
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product.name
    
class Load(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='load_item')
    provider = models.ForeignKey("Provider", on_delete=models.CASCADE, related_name='loads')
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)

    
    class Meta:
        ordering = ('-id',)
        verbose_name = 'Carga'
        verbose_name_plural = 'Cargas'

    def __str__(self):
        return self.product.name


@receiver(post_save, sender=Load)
def save_load(sender, instance, created, **kwargs):
    if created:
        load = instance
        load.product.quantity = load.quantity + load.product.quantity
        load.product.save()

@receiver(post_save, sender=TransferItem)
def save_transfer(sender, instance, created, **kwargs):
    if created:
        transfer = instance
        new_value = transfer.product.quantity - transfer.quantity
        transfer.product.quantity = new_value
        transfer.product.save()
