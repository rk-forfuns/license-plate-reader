from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.log import enable_pretty_logging
from api import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(10111)
enable_pretty_logging()
print "API starting..."
IOLoop.instance().start()