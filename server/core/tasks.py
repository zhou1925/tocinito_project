from requests import get
from bs4 import BeautifulSoup
from celery.utils.log import get_task_logger
from celery import Celery
from celery import shared_task
from .models import Weather

app = Celery()

logger = get_task_logger(__name__)

link = "https://www.senamhi.gob.pe/?p=pronostico-detalle&dp=05&localidad=0017"
data = {}

def get_article(link):
    try:
        r = get(link)
        soup = BeautifulSoup(r.text, 'html.parser')
        article = soup.find("article")
        return article 
    except Exception as e:
        return None

@shared_task
def get_weather():
    data.clear()
    weather_data = ""
    start = 0
    article = get_article(link)
    if article:
        content = [text for text in article.stripped_strings]
        for i in range(len(content)): 
            weather_data = weather_data + content[i] + " "
            if ((i - start + 1) == 5):
                data[len(data) + 1] = weather_data
                weather_data = ""
                start += 5
        weather_obj = Weather.objects.create(data=data)
        weather_obj.save()
    else:
        logger.info("No data")
