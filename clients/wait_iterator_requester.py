""" app """
from tornado import ioloop, gen
from tornado.httpclient import AsyncHTTPClient
from client_utils.constants import URLS

@gen.coroutine
def fetch_and_handle():
    """fetch and handle"""
    http_client = AsyncHTTPClient()
    dic_device = dict()
    arr_req = []
    for index, url in enumerate(URLS):
        dic_device[index] = "custom-request-" + str(index) + ": "
        arr_req.append(http_client.fetch(url))
    
    # start of waiter
    req_waiter = gen.WaitIterator(*arr_req)    
    while not req_waiter.done():
        try:
            result = yield req_waiter.next()
        except Exception as e:
            print("Error {} for request {}".format(e, req_waiter.current_future))
        else:
            index = req_waiter.current_index
            result = result.body
            request_id = dic_device[index]
            print("Result {} received from future {} for {}".format(
                result.decode('utf8'), index, request_id))
    # end of waiter

if __name__ == '__main__':
    LOOP = ioloop.IOLoop.current()
    LOOP.run_sync(fetch_and_handle)
    