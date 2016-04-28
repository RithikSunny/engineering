import scrapy
import urlparse
from os.path import splitext, basename
import os

class CourseSpider(scrapy.Spider):
    name = "CourseSpider"
    # allowed_domains = ["stanford.edu"]
    start_urls = [
        "http://cs224d.stanford.edu/syllabus.html",
    ]

    def print_this_link(self, link):
        print "Link --> {this_link}".format(this_link=link)

    def save_pdf(self, response, base_path='dl_/'):
        # path = self.get_path(response.url)
        filename = base_path + basename(response.url)
        with open(filename, "wb") as f:
            f.write(response.body)

    def save_youtube(self, response, base_path='dl_/'):
        command = "youtube-dl -f 'bestvideo[height<=480]+bestaudio/best[height<=480]' "
        command += response.url
        print command
        os.system(command)

    def parse(self, response):
        print response
        hxs = scrapy.Selector(response)
        # extract all links from page
        all_links = hxs.xpath('*//a/@href').extract()

        print all_links
        print 'size: ', len(all_links)
        # # iterate over links
        for link in all_links:
            if link.endswith('.pdf'):
                # self.save_pdf()
                print 'pdf: ', link
                continue
                link = urlparse.urljoin(response.url, link)
                print 'pdf-v2: ', link
                yield scrapy.http.Request(link, callback=self.save_pdf)
            elif link.startswith('https://youtu.be/'):
                print 'youtube: ', link
                yield scrapy.http.Request(link, callback=self.save_youtube)
            else:
                print 'else: ', link

            # yield scrapy.http.Request(url=link, callback=self.print_this_link)


# def parse_listing(self, response):
#     # ... extract pdf urls
#     for url in pdf_urls:
#         yield Request(url, callback=self.save_pdf)
#
# def save_pdf(self, response):
#     path = self.get_path(response.url)
#     with open(path, "wb") as f:
#         f.write(response.body)