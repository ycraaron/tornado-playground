""" app """
from tornado import ioloop, gen
from tornado.httpclient import AsyncHTTPClient


@gen.coroutine
def fetch_and_handle():
    """fetch and handle"""
    urls = [
        'http://localhost:8899/?device_id=1',
        'http://localhost:8899/?device_id=2',
        'http://localhost:8899/?device_id=3',
        'http://localhost:8899/?device_id=4',
        'http://localhost:8899/?device_id=5'
    ]

    http_client = AsyncHTTPClient()

    req_dic = dict()

    dic_device = dict()
    arr_req = []

    for cnt, url in enumerate(urls):
        req_dic["ambi-device-" + str(cnt) + ": "] = http_client.fetch(url)
        dic_device[cnt] = "ambi-device-" + str(cnt) + ": "
        arr_req.append(http_client.fetch(url))
    
    print(req_dic)
    print(arr_req)
    print(dic_device)

    # start of waiter
    req_waiter = gen.WaitIterator(*arr_req)    
    while not req_waiter.done():
        try:
            result = yield req_waiter.next()
        except Exception as e:
            print("Error {} from {}".format(e, req_waiter.current_future))
        else:
            index = req_waiter.current_index
            comfort = result.body
            device_id = dic_device[index]
            print("Result {} received from future {} for {}".format(
                comfort.decode('utf8'), index, device_id))
            
    # end of waiter

    # start of yield all
    # responses = yield req_dic
    # for key, value in responses.items():
    #     device_id = key
    #     comfort = value.body
    #     print(device_id + comfort.decode('utf8'))
    # end of yield all


# # think about why it won't work
# @gen.coroutine
# def use_iterator(arr_req):
#     print('in waiter')
#     req_waiter = gen.WaitIterator(*arr_req)
#     while not req_waiter.done():
#         print('a')
#         try:
#             print('b')
#             result = yield req_waiter.next()
#             print('c')

#         except Exception as e:
#             print("Error {} from {}".format(e, req_waiter.current_future))
#         else:
#             print('d')

#             print("Result {} received from {} at {}".format(
#                 result.body, req_waiter.current_future,
#                 req_waiter.current_index))
#     print('end')

if __name__ == '__main__':
    LOOP = ioloop.IOLoop.current()
    LOOP.run_sync(fetch_and_handle)
