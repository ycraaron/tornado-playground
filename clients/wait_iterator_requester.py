"""
client
After starting the server, run python wait_iterator_requester.py

"""
from tornado import ioloop, gen
from tornado.httpclient import AsyncHTTPClient
from client_utils.constants import URLS
from client_utils.functions import generate_url
from timeit import default_timer as timer


@gen.coroutine
def fetch_and_handle():
    """fetch and handle"""
    http_client = AsyncHTTPClient()
    dic_device = dict()
    arr_req = []
    URLS = generate_url(5)
    for index, url in enumerate(URLS):
        dic_device[index] = "custom-request-" + str(index) + ": "
        arr_req.append(http_client.fetch(url))

    # start of waiter
    start = timer()
    req_waiter = gen.WaitIterator(*arr_req)
    while not req_waiter.done():
        try:
            result = yield req_waiter.next()
        except Exception as e:
            index = req_waiter.current_index
            # print('index exception', index)
            print("Error {} for request {}".format(
                e, req_waiter.current_future))
        else:
            index = req_waiter.current_index
            # print('index', index)
            result = result.body
            request_id = dic_device[index]
            print("{} back and start to work for 1 second".format(
                index
            ))
            yield gen.sleep(1)
            print("{} finish sleeping".format(
                index
            ))
            # print("Result {} received from future {} for {}".format(
            #     result.decode('utf8'), index, request_id))
    end = timer()
    print(end - start)
    # end of waiter


if __name__ == '__main__':
    LOOP = ioloop.IOLoop.current()
    LOOP.run_sync(fetch_and_handle)
