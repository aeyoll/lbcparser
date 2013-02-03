import web
import config

import urllib2
from bs4 import BeautifulSoup

import re
import urllib


t_globals = dict(
datestr=web.datestr,
)
render = web.template.render('templates/', cache=config.cache,
    globals=t_globals)
render._keywords['globals']['render'] = render


def form(**k):
    return render.form()


def listing(url, **k):
    print url
    url = urllib.unquote(url)

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
            annonce_data['date'] = date[0].div.string
            if image:
                annonce_data['image'] = image[0]
            else:
                annonce_data['image'] = ''
            annonce_data['link'] = link
            annonce_data['location'] = re.sub(' +', ' ', location[0].string)
            if price:
                annonce_data['price'] = price[0].string
            else:
                annonce_data['price'] = '0'
            annonce_data['title'] = title[0].string
            annonces.append(annonce_data)

        return render.listing(annonces)
