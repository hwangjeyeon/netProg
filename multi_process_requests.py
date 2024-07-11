import requests, time
import multiprocessing

session = None

def get_session():
    global session
    if not session:
        session = requests.Session()

def download_site(url):
    with session.get(url) as response:
        name = multiprocessing.current_process().name
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    with multiprocessing.Pool(processes=5, initializer=get_session) as pool:
        pool.map(download_site, sites)

