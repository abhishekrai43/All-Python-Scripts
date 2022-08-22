import requests
import concurrent
from concurrent import futures
import requests

def request_post(ur):
    site = requests.get(ur)
    print(site.url)

with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor: # optimally defined number of threads
    urls = "https://t.co/4FLCR92Vmy", "https://t.co/5BkmAFYF2K", "https://t.co/c95ibuDuQB"
    res = [executor.submit(request_post, ur) for ur in urls]
    concurrent.futures.wait(res)







