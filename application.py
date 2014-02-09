#!/usr/bin/env python

import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options

define("port", default=8888, help="Run app on the given port", type=int)

import dbconf

class Application(tornado.web.Application):
    ## Application setup 
    def __init__(self):
        from handlers import handlers
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=True,
            cookie_secret="$0m#Rand0m5+r1ng",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)
        self.db=dbconf.db

        
## Starts the application
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
