def generate_url(num = 5000):
    arr_urls = []
    url = "http://localhost:8899/?param={}"
    for i in range(num):
        arr_urls.append(url.format(i))
    return arr_urls
