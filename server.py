#!/usr/bin/env python
# coding=utf-8
import web
import controller

urls = (
    "/api/null", "Index",
    "/api/public", controller.public
)

class Index:
    def GET(self):
        return "success"


web.config.debug = True
app = web.application(urls,locals(),autoreload=True)

if __name__ == "__main__":
    app.run()
else:
    application = app.wsgifunc()
