#!/usr/bin/env python
import os
import asyncio
from django.core.wsgi import get_wsgi_application
import tornado
import tornado.ioloop
import tornado.web
import tornado.wsgi
import argparse
from sockjs.tornado import SockJSRouter
from tornado.platform.asyncio import AsyncIOMainLoop
from snugdc.sockjs import SNUGDCConnection

# Parse arguments
ARGS = argparse.ArgumentParser(description="Run simple http server.")
ARGS.add_argument(
    '--port', action="store", dest='port',
    default=8008, type=int, help='Port number')
args = ARGS.parse_args()

def main():
    # Create Django WSGI App
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "snugdc.settings")
    django_app = get_wsgi_application()
    wsgi_app = tornado.wsgi.WSGIContainer(django_app)

    sockjs_router = SockJSRouter(SNUGDCConnection, '/ws')
    wsgi_urls = [('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app))]
    app = tornado.web.Application(sockjs_router.urls + wsgi_urls)
    app.listen(args.port)
    tornado.ioloop.IOLoop.configure('tornado.platform.asyncio.AsyncIOLoop')
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()
