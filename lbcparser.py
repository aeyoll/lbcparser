import web
import view
from view import render
from urlparse import urlparse


urls = (
    '/', 'index',
    '/url', 'url'
)


class index:
    def GET(self):
        return render.base(view.form())


class url:
    def GET(self):
        form = web.input()
        url = form.url
        o = urlparse(url)
        if o.netloc == 'www.leboncoin.fr':
            web.header('Content-Type', 'text/xml')
            # return render.response(code)
            return view.listing(url)
        else:
            return ''


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
