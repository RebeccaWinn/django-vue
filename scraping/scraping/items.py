# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy_djangoitem import DjangoItem
from calendar_events.models import ScrapingItem
import scrapy


class ScrapingItem(DjangoItem):
    # define the fields for your item here like:
    django_model = ScrapingItem
   