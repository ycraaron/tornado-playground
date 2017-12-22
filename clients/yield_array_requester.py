"""
client
After starting the server, run python yield_array_requester.py
"""

from tornado import ioloop, gen
from tornado.httpclient import AsyncHTTPClient
from timeit import default_timer as timer
from client_utils.constants import URLS
from client_utils.functions import generate_url


@gen.coroutine
def fetch_and_handle():
    """fetch and handle"""

    http_client = AsyncHTTPClient()

    req_dic = dict()

    URLS = generate_url(5)
    for cnt, url in enumerate(URLS):
        req_dic["custom-request-" + str(cnt) + ": "] = http_client.fetch(url)
    # start of yield all
    start = timer()
    responses = yield req_dic
    for key, value in responses.items():
        device_id = key
        return_value = value.body
        print("{} back and start to work for 1 second".format(
            device_id
        ))
        yield gen.sleep(1)
        print("{} finish sleeping".format(
            device_id
        ))
    end = timer()
    # end of yield all
    print(end - start)


if __name__ == '__main__':
    LOOP = ioloop.IOLoop.current()
    LOOP.run_sync(fetch_and_handle)
