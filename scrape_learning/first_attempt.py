# coding:utf-8
"""
    A folder that store many files that scrape the web for educational purposes
    Current target: my school blog
"""
__author__ = "Reni A. Dantas"
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote
from bs4 import BeautifulSoup
from os import chdir, getcwd


class BloggerScrapper(object):
    """ Module that extracts data """
    def __init__(self, target):
        self.target = target
        self.soup = BeautifulSoup(self.get(), 'html.parser')

    def get(self):
        """ Get a response """
        try:
            return urlopen(self.target).read()
        except Exception as e:
            raise Exception(e)

    def all_links(self):
        """ Getting all links from this this """
        return self.soup.findAll('a')

    def get_fpost(self):
        """ Get a photo from featured photo if exists """
        try:
            featured_post = self.soup.find('div', {'class': 'widget FeaturedPost'})
            return featured_post.find('img')['src']
        except Exception as e:
            raise Exception(e)

    def get_posts(self, save=False):
        """ Get all posts """
        def download_image(url):
            """ Download a picture """
            fname = url[::-1]
            fname = fname[:fname.find('/'):]
            fname = fname[::-1].replace('%', '')
            try:
                urlretrieve(url, fname)
            except Exception as e:
                raise Exception(e)
        try:
            chdir("images") if save else chdir(getcwd())
            content = self.soup.find('div', {'class': 'blog-posts hfeed'})
            posts = [x for x in content.findAll('div', {'class': 'date-outer'})]
            for post in posts:
                post_image = None
                title_post = post.find('h3', {'class': 'post-title entry-title'}).text.strip()
                posts_feed = post.find('div', {'class': 'post-outer'})
                post_content = posts_feed.find('div', {'class', 'post-body entry-content'})
                try:
                    post_image = post_content.find('div', {'class': 'separator'}).find('a')['href']
                    download_image(post_image) if save else None
                except AttributeError:
                    pass
                except TypeError:
                    pass
                post_text = [text.text.strip() for text in  post_content.findAll('div', {'style': 'text-align: justify;'})]
                yield title_post, post_text, post_image
        except Exception as e:
            raise Exception(e)

bs = BloggerScrapper(r'http://josegvieira.blogspot.com.br/search?max-results=55')
for post in bs.get_posts(save=1):
	print(post)
