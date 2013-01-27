import web
import view
from view import render


urls = (
    '/', 'index',
    '/url', 'url'
)


class index:
    def GET(self):
        return render.base(view.form())


class url:
    def GET(self):
        # return "%s %s\n" % (name, url)
        form = web.input()
        url = form.url
        return render.base(view.listing(url))


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.internalerror = web.debugerror
    app.run()
