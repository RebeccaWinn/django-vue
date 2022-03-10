import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
        
        
        # https://www.self.com/fitness/workouts
       # https://lifehacker.com/health/fitness
       #https://www.muscleandfitness.com/workout-routines/
       #https://www.muscleandfitness.com/workouts/workout-tips/
       #https://www.bodybuilding.com/recipes
      # https://healthyfitnessmeals.com/blog/
       #https://www.muscleandstrength.com/workout-routines
class FitnessWorkoutSpider(scrapy.Spider):
    name = "workouts"
    def start_requests(self):
        urls = [
            'https://www.muscleandfitness.com/workout-routines/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
            
            

           

       
