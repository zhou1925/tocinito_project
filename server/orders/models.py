from django.db import models
  
class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField(blank=True)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField("Precio", max_digits=10, decimal_places=2)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
                                        
    def __str__(self):
        return self.title
                                    
class Order(models.Model):
    date_stamp = models.DateField(auto_now_add=True)
    time_stamp = models.TimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'

    @property
    def items_count(self):
        """ return total order in products """
        return sum(item.quantity for item in self.items.all())
    
    @property
    def total(self):
        """ return total sum of products in order """
        total = 0
        for item in self.items.all():
            total += int(item.quantity) * float(item.product.price)
        return total
    
    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("Cantidad",default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    class Meta:
        verbose_name = "item"
        verbose_name_plural = "items"
        unique_together = (
            ('product', 'order')
        )

    def __str__(self):
        return self.product.title

