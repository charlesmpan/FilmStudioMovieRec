import scrapy


class ParamountSpider(scrapy.Spider):
    name = 'paramount'
    allowed_domains = ['www.the-numbers.com']
    start_urls = ['https://www.the-numbers.com/box-office-records/worldwide/all-movies/theatrical-distributors/paramount-pictures']

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
