from urllib.parse import quote
from ..items import ScrapingItem
import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'https://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
            
            
        # https://www.self.com/fitness/workouts
       # https://lifehacker.com/health/fitness
   
       #https://www.bodybuilding.com/recipes
      # https://healthyfitnessmeals.com/blog/
       #https://www.muscleandstrength.com/workout-routines
       
class FitnessWorkoutSpider(scrapy.Spider):
    name = "workouts"
    #add in the categories
    def start_requests(self):
        url = 'https://www.muscleandfitness.com/workouts/full-body/'
        yield scrapy.Request(url, self.parse)
        #yield scrapy.Request(f'https://www.muscleandfitness.com/workout-routines/{self.category}')
    def parse(self,response):
        workouts = response.css('.l-main__content .article')
        for article in workouts:
            item = ScrapingItem()
            item['category'] = "full-body"
            item['title'] = article.css('h3 a::text').extract()
            item['link'] = article.css('.article__title a::attr(href)').extract_first()
            item['img'] = article.css('div img::attr(src)').extract_first()
            yield item
            
                 
class FitnessTipsSpider(scrapy.Spider):
    name = "workout_tips"
    def start_requests(self):
        url = 'https://www.muscleandfitness.com/workouts/workout-tips/'
        yield scrapy.Request(url, self.parse)
    def parse(self,response):
        workouts = response.css('.l-main__content .article')
        for article in workouts:
            item = ScrapingItem()
            item['category'] = "tips"
            item['title'] = article.css('h3 a::text').extract()
            item['link'] = article.css('.article__title a::attr(href)').extract_first()
            item['img'] = article.css('div img::attr(src)').extract_first()
            yield item
class FitnessTipsAndWorkoutsSpider(scrapy.Spider):
    name = "moreworkouts"
    def start_requests(self):
        url = 'https://www.self.com/fitness/workouts/'
        yield scrapy.Request(url, self.parse)
    def parse(self,response):
        for article in response.css('.river-item'):
            yield {
                'title':article.css('.river-item-content a ::text').get(),
                'img':article.css('.component-responsive-image img').get(),
            }
         

       
