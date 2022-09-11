from django.utils import timezone
from datetime import timedelta
from orders.models import Order
from sales.models import Sale
from celery.utils.log import get_task_logger
from celery import Celery
from celery import shared_task


app = Celery()

logger = get_task_logger(__name__)

@shared_task
def save_today_sale():
    """
    compute sales by day
    """
    logger.info("Save sale start...")
    total_sale = 0
    orders = Order.objects.filter(date_stamp=timezone.now() - timedelta(days=1))
    
    for order in orders:
        total_sale += order.total
    
    sale = Sale.objects.create(amount=total_sale)
    sale.save()
    logger.info("Save sale finished...")

