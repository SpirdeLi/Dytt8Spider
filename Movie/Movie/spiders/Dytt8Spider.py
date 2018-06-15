import scrapy
from Movie.items import MovieItem
from scrapy import Selector

class Dytt8Spider(scrapy.Spider):
    #爬虫的名字
    name = "Dytt8"
    #允许的域名
    allowed_domains = ["dytt8.net"]
    start_urls = [
        "http://www.dytt8.net/html/gndy/dyzz/index.html"
    ]
    def parse(self,response):
        Baseurl = "http://www.dytt8.net"
        contents = response.xpath("//div[@class='co_content8']/ul/td/table/tr[2]/td[2]/b")
        for content in contents:
            Movieurl = content.xpath(".//a/@href").extract()[0]
            Movieurl = Baseurl + str(Movieurl)
            Moviename = content.xpath(".//a/text()").extract()
            if len(Moviename) == 0:
                Moviename = content.xpath(".//b/text()").extract()[0]
            else:
                Moviename = content.xpath(".//a/text()").extract()[0]
            request = scrapy.Request(url = Movieurl,callback=self.MovieInfomation)
            request.meta['Movieurl'] = Movieurl
            request.meta['Moviename'] = Moviename
            yield request
        next_page = Selector(response).re('<a href="(.*?)">下一页</a>')
        if next_page:
            preurl = "http://www.dytt8.net/html/gndy/dyzz/"
            url = preurl + next_page[0]
            yield scrapy.Request(url = url,callback=self.parse)

    def MovieInfomation(self,response):
        Movieurl = response.meta['Movieurl']
        Moviename = response.meta['Moviename']
        Image = response.xpath("//div[@id='Zoom']//img/@src").extract()
        contents = response.xpath("//div[@id='Zoom']//text()").extract()
        for index,content in enumerate(contents):
            if content.startswith("◎类\u3000\u3000别") or content.startswith("◎电影类型"):
                Moviecategory = content.replace('◎类\u3000\u3000别','').strip()
            if content.startswith("◎主\u3000\u3000演"):
                actors = ""
                actor = content.replace('◎主\u3000\u3000演','').strip()
                actors = actors + actor
                for x in range(index+1,len(contents)):
                    value = contents[x].strip()
                    if value.startswith("◎简\u3000\u3000介") or value.startswith("简\u3000\u3000介"):
                        break
                    else:
                        actors = actors + value
                if len(actors)==0:
                    actors = "不详"
            if content.startswith("◎简\u3000\u3000介") or content.startswith("简\u3000\u3000介"):
                Introductions = ""
                Introduction = content.replace('简\u3000\u3000介','').strip()
                Introductions = Introductions + Introduction
                for x in range(index+1,len(contents)):
                    value = contents[x].strip()
                    if value.startswith("【下载地址】"):
                        break
                    elif len(value)==0:
                        pass
                    else:
                        Introductions = Introductions + value
            if content.startswith("【下载地址】"):
                Downloads = []
                for x in range(index+1,len(contents)):
                    value = contents[x].strip()
                    if len(value)==0:
                        pass
                    else:
                        Downloads.append(value)
        item = MovieItem(Movieurl = Movieurl,Moviename = Moviename,Image = Image[0],Moviecategory = Moviecategory,actors = actors,Introductions=Introductions,Downloadurl = Downloads[0])
        yield item









