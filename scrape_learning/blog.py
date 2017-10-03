from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
import random
import os


class Scrapper(object):
    def __init__(self):
        self.link ="https://josegvieira.blogspot.com.br/"
        self.headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
        self.response = self._get()
        self.soup = BeautifulSoup(self.response, 'lxml')

    def _get(self):
        try:
            return urlopen(Request(self.link, None, self.headers)).read()
        except Exception as e:
            pass

    def _enter_folder(self):
        if not os.path.exists('data'):
            os.mkdir('data')
        os.chdir('data')

    def get_highlighted_post(self):
        soup = self.soup
        widget_featured_post = soup.find('div', {'class': 'widget FeaturedPost'})
        widget_content = widget_featured_post.find('div', {'class': 'widget-content'})
        article = widget_content.find('article', {'class': 'post'})
        title = article.h3.text.strip()
        post_date = article.find('span', {'class': 'byline post-timestamp'}).a.text.strip()
        print title, post_date

    def get_all_posts(self):
        soup = self.soup
        blog_posts = soup.find('div', {'class': 'blog-posts hfeed container'})
        articles = [article for article in blog_posts.findAll('article')]
        self._enter_folder()
        for article in articles:
            post = article.find('div', {'class': 'post'})
            post_title = post.h3.text.strip()
            post_date = post.find('span', {'class': 'byline post-timestamp'}).a.text.strip()
            content = post.find('div', {'class': 'container post-body entry-content'})
            try:
                thumbnail = content.find('div', {'class': 'snippet-thumbnail'}).img.get('src').strip()
                data = urlopen(thumbnail).read()
                with open(str(random.randint(0, 9999))+'.jpg', 'wb') as f:
                    f.write(data)
            except Exception as e:
                thumbnail = None
            print post_title, post_date, thumbnail
        else:

scrap = Scrapper()
scrap.get_all_posts()