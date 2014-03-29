from __future__ import absolute_import

from sockjs.tornado import SockJSConnection

__all__ = ('SNUGDCConnection',)

class SNUGDCConnection(SockJSConnection):
    def on_message(self, msg):
        self.send(msg)
