# -*- coding:utf-8 -*-
# Created by shellbye on 2018/1/3.
# http://lucumr.pocoo.org/2007/5/21/getting-started-with-wsgi/

HELLO_WORLD = b"Hello! world!\n"


def simple_app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return [HELLO_WORLD]

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8090, simple_app)
    srv.serve_forever()
