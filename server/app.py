"""
server
"""
from tornado import ioloop, gen, web
from tornado.web import RequestHandler
from datetime import datetime
from timeit import default_timer as timer

class MainHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        str_device_id = self.get_query_argument('device_id')
        str_datetime = datetime.now()
        print(str_datetime)
        print("device_id", str_device_id)
        print(type(str_device_id))
        if(str_device_id == '5'):
            print("before gen sleep")
            yield gen.sleep(5)
            self.set_status(400)
            self.write('error')
        self.write(str(int(str_device_id)/10))

def make_app():
    return web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    APP = make_app()
    APP.listen(8899)
    ioloop.IOLoop.current().start()