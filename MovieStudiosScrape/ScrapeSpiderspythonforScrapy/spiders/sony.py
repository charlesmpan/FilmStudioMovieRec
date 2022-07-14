import scrapy
import logging

class SonySpider(scrapy.Spider):
    name = 'sony'
    allowed_domains = ['www.the-numbers.com']
    start_urls = ['https://www.the-numbers.com/box-office-records/worldwide/all-movies/theatrical-distributors/sony-pictures']
    headers = {'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    def parse(self, response):
        
        
        
        

        year_released = response.xpath('.//*[@id="page_filling_chart"]/center/table/tbody/tr//td[2]//a/text()').getall()
        movie_name = response.xpath('.//*[@id="page_filling_chart"]/center/table/tbody/tr//td//b//a/text()').getall()
        worldwide_box =response.xpath('.//*[@id="page_filling_chart"]/center/table/tbody/tr//td[4]/text()').getall()
        domestic_box = response.xpath('.//*[@id="page_filling_chart"]/center/table/tbody/tr//td[5]/text()').getall()
        international_box = response.xpath('.//*[@id="page_filling_chart"]/center/table/tbody/tr//td[6]/text()').getall()

        yield {
                'year released' : year_released,
                'movie name' : movie_name,
                'worldwide box':worldwide_box,
                'domestic box':domestic_box,
                'international box':international_box
            }
