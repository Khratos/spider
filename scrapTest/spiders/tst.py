import scrapy
# import json


# class QuotesSpider(scrapy.Spider):
#     name = "quote"
#     allowed_domains = ['quotes.toscrape.com']
#     page = 1
#     start_urls = ['http://quotes.toscrape.com/api/quotes?page=1']

#     def parse(self, response):
#         data = json.loads(response.text)
#         for quote in data["quotes"]:
#             yield {"quote": quote["text"]}
#         if data["has_next"]:
#             self.page += 1
#             url = f"http://quotes.toscrape.com/api/quotes?page={self.page}"
#             yield scrapy.Request(url=url, callback=self.parse)
#         filename = f'quotes-{page}.txt'
#         with open(filename, 'wb') as f:
#             f.write(response.body)        

# mport scrapy

# class Items(scrapy.Item):
#     # define the fields for your item here like:
#     link = scrapy.Field()
#     sku = scrapy.Field()
#     name = scrapy.Field()

class ProductosSpider(scrapy.Spider):
    #abrir documento
    name = "productos"
    allowed_domains = ["www.chedraui.com.mx","chedraui.com.mx"]
    #start_urls = ['https://www.chedraui.com.mx/search?text=jicama%20precortada&method=enter' ]
    BASE_URL = 'https://www.chedraui.com.mx'
    #https://www.chedraui.com.mx/Departamentos/c/MC?q=%3Arelevance&page=4&pageSize=24
    # % page for page in xrange(1,54)
    def start_requests(self):
        
        urls = "https://www.chedraui.com.mx/search?text=jicama%20precortada&method=enter"
        yield scrapy.Request(url, callback=self.parse)
            
   
    def parse(self, response):
        links = response.xpath('//a[@class="product__list--thumb"]/@href').extract()
        for link in links:
            absolute_url = self.BASE_URL + link
            yield scrapy.Request(absolute_url, callback=self.parse_attr)   

    def parse_attr(self, response):
            item = Items()
            item["link"] = response.url
            item["sku"] = "".join(response.xpath("//span[@class='code']//text()").extract())
            item["name"] = "".join(response.xpath("//div[@class='product-details-name name']//text()").extract())
            return item



#             import scrapy
# import json
# import openpyxl
# from openpyxl import Workbook


# class Items(scrapy.Item):
#     #link = scrapy.Field()
#     sku = scrapy.Field()
#     name = scrapy.Field()

    
# class UPCSpider(scrapy.Spider):
#     name = "upc"
#     allowed_domains = ["www.chedraui.com.mx","chedraui.com.mx"]
#     #start_urls = ['https://www.chedraui.com.mx/search?text=jicama&method=enter']
#     BASE_URL = 'https://www.chedraui.com.mx'
#     iter = 2
#     item = Items()
#     def start_requests(self):
#         with open ('Listado_Productos-1.txt', 'r') as f:  
#             fout = open("out.txt", "wt") 
#             # res = f.replace (u" ", u"%20")                
#             # print(res)
#             for ugly in f:
#                 fout.write(ugly.replace(' ', '%20'))
#                 #print(ugly.replace(' ', '%20'))
#             fout.close()
#         f.close()
#         with open ('out.txt', 'r') as fout:             
#             for pretty in fout:                                
#                 urls = f"https://www.chedraui.com.mx/search?text={pretty}&method=enter"
#             # for url in urls:
#                 #print("absolut" + absolute_url)   
#                 yield scrapy.Request(url=urls, callback=self.parse)  
#         fout.close() 

# #productClickData_plp_name_[i]
#     def parse(self, response):
      
#         print ("RESPONSE CONTETN" + response.content)
#         # self.iter = self.iter + 1
#         # wb = Workbook()
#         # ws = wb.active
#         # in_sku =  ws['A1'] = "UPC"
#         # in_name = ws['B1'] = "Producto"    
#         # row_tuple = (in_sku, in_name)
#         # listenings = response.xpath('//a[@class="product__list--thumb"]/@href').extract() 
#         # for link in listenings:
#         #     print("oooooo" + link)
#                 #print(urld)
#                     # print(prod)
#                     # strsplit =  res.split()
#                     # print(str)
           
#         links = response.xpath('//a[@class="product__list--thumb"]/@href').extract()
#         print("oooooo" + links)
#         for link in links:
#             absolute_url = self.BASE_URL + link
#             yield scrapy.Request(absolute_url, callback=self.parse_attr)
            
#         #print("x" + x)
#         # for i, elem in x:
#         #     print("prrrrr" + elem["sku"])
#         #     ws['A' + str(i)] = elem["sku"]
#         #     ws['B' + str(i)] = elem["name"]
#         #     print(i)
#         #     wb.save("sample.xlsx")   
      
 
        
#     def parse_attr(self,response):
#         item = Items()
#         #ws = wb.load_workbook("sample.xlsx")
       
      
       
#         #self.item["link"] = response.url
#         self.item["sku"] = "".join(response.xpath("//span[@class='code']//text()").extract())
#         self.item["name"] = "".join(response.xpath("//div[@class='product-details-name name']//text()").extract())
#        # print('A' + str(self.iter))

        
#         # ws.append()
#         # in_sku =  ws['A' + str(self.iter)] = ("".join(response.xpath("//span[@class='code']//text()").extract()))
#         # in_name = ws['B' + str(self.iter)] = ("".join(response.xpath("//div[@class='product-details-name name']//text()").extract()))
        
#         # ws.append(row_tuple)
        
#         #print(iter)
#         # with open(filename, 'w') as f:
#         #         f.write(str(bytes(item["link"], encoding='UTF-8')))
#         # f.close()     
       
                      
#         return item
#     #      item = []
#             #xp = response.xpath("//ul[@id='plp_display']//li").extract()
            
#             # print( response.css('title::text').get())
#             # print(response.selector.xpath('//title/text()'))
#             # print(response.css)
#             # doc = ""
#         # print(response.selector.xpath('//ul[@class, "product__listing product__grid"]'))
#             # print(response.selector.xpath('//input[contains(@class, "productClickData_plp_name_0")]/@value').extract())
#             # print(response.selector.xpath('//input[contains(@class, "productClickData_plp_name_\d$")]/@value').extract())
       
#            # self.log(r)
           
#        # filename = f'search.txt'
#       #  self.log(response)
#         # with open(filename, 'wb') as f:
#         #     line = json.dumps(dict())
#         #     f.write(item[0])
#         # self.log(f'Saved file {filename}')
#         # try:
#         #     print("Give a element to search")
#         #     element = input()
#         #     res = element.replace (u" ", u"%20")
#         #     data = json.loads(response.text)
#         #     if data:
#         #         for dt in data["product__list--item"]:
#         #             self.log(dt)
#         #     #   item = {}
#         #             yield {"productClickData_plp_name_": dt["text"]}
#         #         if data["has_next"]:
#         #             url = f"https://www.chedraui.com.mx/search?text={res}&method=enter"
#         #     #         #print(url)
#         #             yield scrapy.Request(url=url, callback=self.parse )
           
#         # except ValueError as e:  # includes simplejson.decoder.JSONDecodeError
#         #     print ('Decoding json failed', e)
        