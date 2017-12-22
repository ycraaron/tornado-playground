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
        str_param = self.get_query_argument('param')
        print('start to sleep for {} seconds'.format(
            str_param
        ))

        # yield gen.sleep(int(str_param))
        yield gen.sleep(1)
        print('end to sleep for {} seconds'.format(
            str_param
        ))
        print("param", str_param)
        # START
        # uncomment following code to test http request failure
        # if(str_param == '4'):
        #     self.set_status(400)
        #     self.write('error')
        # END
        self.write(str(int(str_param) / 10))


def make_app():
    return web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    APP = make_app()
    APP.listen(8899)
    ioloop.IOLoop.current().start()
