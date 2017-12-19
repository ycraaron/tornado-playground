""" app """
from tornado import ioloop, gen
from tornado.httpclient import AsyncHTTPClient
from client_utils.constants import URLS


@gen.coroutine
def fetch_and_handle():
    """fetch and handle"""

    http_client = AsyncHTTPClient()

    req_dic = dict()

    for cnt, url in enumerate(URLS):
        req_dic["custom-request-" + str(cnt) + ": "] = http_client.fetch(url)

    # start of yield all
    responses = yield req_dic
    for key, value in responses.items():
        device_id = key
        comfort = value.body
        print(device_id + comfort.decode('utf8'))
    # end of yield all

if __name__ == '__main__':
    LOOP = ioloop.IOLoop.current()
    LOOP.run_sync(fetch_and_handle)

