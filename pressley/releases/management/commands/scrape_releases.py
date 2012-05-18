from django.core.management.base import BaseCommand, CommandError
from releases.models import Release
from sources.models import Source
from readability.readability import Document
from lxml import etree, html
from dateutil.parser import parse
from util import condense_whitespace
import requests

class Command(BaseCommand):
    args = '<none>'
    help = "Scrapes rss feeds in database for releases"
    
    def get_link_content(self, link):
        content = requests.get(link).content
        readable = Document(content)
        body = html.fromstring(readable.summary()).text_content()
        return condense_whitespace(body)


    def handle(self, *args, **kwargs):

        sources = Source.objects.filter(source_type=2)
        for source in sources:
            print source.url
            feed = requests.get(source.url).content
            feed_tree = etree.fromstring(feed)
            for item in feed_tree.iter('item'):
                
                source_name = source.organization
                date = parse(item.find('pubDate').text)
                title = item.find('pubDate').text 
                link = item.find('link').text
                
                body = self.get_link_content(link)

                release = Release.objects.get_or_create(url=link, title=title, date=date, body=body, source=source)

#            print feed.content            
        