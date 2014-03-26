#!/usr/bin/env python
import os
import asyncio
from django.core.wsgi import get_wsgi_application
from aiohttp.wsgi import WSGIServerHttpProtocol
import argparse

# Parse arguments
ARGS = argparse.ArgumentParser(description="Run simple http server.")
ARGS.add_argument(
    '--host', action="store", dest='host',
    default='0.0.0.0', help='Host name')
ARGS.add_argument(
    '--port', action="store", dest='port',
    default=8008, type=int, help='Port number')
args = ARGS.parse_args()
if ':' in args.host:
    args.host, port = args.host.split(':', 1)
    args.port = int(port)

def main():
    # Create Django WSGI App
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blackboard.settings")
    django_app = get_wsgi_application()

    # Get event loop and
    loop = asyncio.get_event_loop()
    
    # Run!
    wsgi_server = lambda: WSGIServerHttpProtocol(django_app)
    f = loop.create_server(wsgi_server, args.host, args.port)
    svr = loop.run_until_complete(f)

    socks = svr.sockets
    print('serving on', socks[0].getsockname())
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()

