"""
server
Open terminal, run python3 app.py to start the server.
"""
from datetime import datetime
from tornado import ioloop, gen, web
from tornado.web import RequestHandler

class MainHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        str_device_id = self.get_query_argument('param')
        str_datetime = datetime.now()
        print(str_datetime)
        print("param", str_device_id)
        print(type(str_device_id))
        if(str_device_id == '4'):
            print("before gen sleep")
            yield gen.sleep(4)
            # START
            # uncomment following code to test http request failure
            # self.set_status(400)
            # self.write('error')
            # END
        self.write(str(int(str_device_id)/10))

def make_app():
    return web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    APP = make_app()
    APP.listen(8899)
    ioloop.IOLoop.current().start()