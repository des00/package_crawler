# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 15:03:38 2017

@author: nodstream
"""

import scrapy


class PackageSpider(scrapy.Spider):
    name = "yorkcity"

    def start_requests(self):
        urls = [
              #'https://play.google.com/store/apps'
              'https://play.google.com/store/apps/details?id=com.kakao.talk.theme.ryan'
#            'http://quotes.toscrape.com/page/1/',
#            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        
        category_results = response.css('a.document-subtitle.category::attr(href)').extract_first()
        category_results_str = category_results.split("/")
        
        if (len(category_results) > 0 and len(category_results_str) > 0):
            category = category_results_str[-1]
        else:
            category = "NA"
        
        self.log('category list is %s' % category_results)
        self.log('category string is %s' % category_results_str)
        self.log('category is %s' % category)