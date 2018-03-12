# -*- coding:utf-8 -*- 
import scrapy 
class ShiyanlouCoursesSpider(scrapy.Spider):
    """all Scrapy spider need to write a Spider class, this class need to inherit Scrapy.Spider classs./ in this class define web and url need to requst \ and how to return data scrapy from website ...etc 
    """

# Spider indenfy sign ,in scrapy project maybe need not only one spider, Name is used to indenitfy every spider,can not to be same  

    name='shiyanlou-courses'
    @property
    def start_requests(self):
        url_tmpl='https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&all&tag=all&page={}' 
        urls=(url_tmpl.format(i) for i in range(1,23))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parase)

    def parse(self,response):
        for course in response.css('div.course-body'):
            yield{
                    #name course
                    'name':course.css('div.course-name::text').extract_first(),
#kecheng miaoshi 
                    'description':course.css('div.course-desc::text').extract_first(),
                    'type':course.css('div.course-footerspan.pull-right::text').extract_first(default='Free'),
                    'students':course.xpath('.//span[contains(@cllass,"pull-left")]/text()[2]').re_first('[^\d]*(\d+)[^\d]*')
                    }


        pass 

