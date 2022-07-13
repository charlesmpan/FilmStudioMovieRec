import scrapy


class ActorsSpider(scrapy.Spider):
    name = 'actors'
    allowed_domains = ['www.the-numbers.com']
    start_urls = ['https://www.the-numbers.com/box-office-star-records/worldwide/lifetime-acting/top-grossing-leading-stars']

    def parse(self, response):
        
        actor_name = response.xpath('/html/body/div/div[3]/div[5]/center/table/tbody/tr/td/b/a/text()').getall()
        movie_average_yield = response.xpath('//html/body/div/div[3]/div[5]/center/table/tbody/tr/td[5]/text()').getall()

        yield {
            'actor' : actor_name,
            'Gross Earnings by movie starred in / number of movies starred in' : movie_average_yield


        }