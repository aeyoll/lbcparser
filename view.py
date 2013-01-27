import web
import config

import urllib2
from bs4 import BeautifulSoup

import re

t_globals = dict(
datestr=web.datestr,
)
render = web.template.render('templates/', cache=config.cache,
    globals=t_globals)
render._keywords['globals']['render'] = render


def listing(**k):

    url = 'http://www.leboncoin.fr/instruments_de_musique/offres/'\
    'aquitaine/occasions/?f=a&th=1&q=sunn'

    soup = BeautifulSoup(
        urllib2.urlopen(url).read())

    for row in soup.find_all('div', 'list-lbc'):
        annonce = row('a')
        annonces = []
        for lbc in annonce:
            annonce_data = {}
            date = lbc('div', 'date')
            image = lbc('img')
            link = lbc['href']
            location = lbc('div', 'placement')
            price = lbc('div', 'price')
            title = lbc('div', 'title')
            # print date[0].div.string
            # print image[0]
            # print re.sub(' +', ' ', location[0].string)
            # print link
            # print price[0].string
            # print title[0].string
            annonce_data['date'] = date[0].div.string
            annonce_data['image'] = image[0]
            annonce_data['link'] = link
            annonce_data['location'] = re.sub(' +', ' ', location[0].string)
            annonce_data['price'] = price[0].string
            annonce_data['title'] = title[0].string
            annonces.append(annonce_data)
            # print annonce_data

        return render.listing(annonces)
