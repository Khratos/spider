import scrapy
from openpyxl import Workbook

class Items(scrapy.Item):
    #link = scrapy.Field()
    sku = scrapy.Field()
    name = scrapy.Field()
    
class UPCSpider(scrapy.Spider):
    name = "upc"
    allowed_domains = ["www.chedraui.com.mx","chedraui.com.mx"]
    #start_urls = ['https://www.chedraui.com.mx/search?text=jicama&method=enter']
    BASE_URL = 'https://www.chedraui.com.mx'
 
    def start_requests(self):
        with open ('Listado_Productos-1.txt', 'r') as f:  
            fout = open("out.txt", "wt") 
            for ugly in f:
                fout.write(ugly.replace(' ', '%20'))
            fout.close()
        f.close()
        with open ('out.txt', 'r') as fout:             
            for pretty in fout:                                
                urls = f"https://www.chedraui.com.mx/search?text={pretty}&method=enter"
                yield scrapy.Request(url=urls, callback=self.parse)  
        fout.close() 

#productClickData_plp_name_[i]
    def parse(self, response):   
        links = response.xpath('//a[@class="product__list--thumb"]/@href').extract()
        for link in links:
            absolute_url = self.BASE_URL + link
            yield scrapy.Request(absolute_url, callback=self.parse_attr)
 
    def parse_attr(self,response):
        item = Items()
        item["sku"] = "".join(response.xpath("//span[@class='code']//text()").extract())
        item["name"] = "".join(response.xpath("//div[@class='product-details-name name']//text()").extract())

        return item
       