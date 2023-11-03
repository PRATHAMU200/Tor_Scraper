import requests
import sys
from colorama import Fore, Back, Style
import threading
from bs4 import BeautifulSoup
def get_tor_session():
    session = requests.session()
    # Tor uses the 9050 port as the default socks port
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

session = get_tor_session()
#url = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q=hello"
if "-u" in sys.argv:
    url = sys.argv[sys.argv.index("-u") + 1]
if "-o" in sys.argv:
    file = sys.argv[sys.argv.index("-o") + 1]
reqs = session.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
with open(file,'a') as f:
    for link in soup.find_all('a'):
        print(link.get('href'))
        f.write(link.get('href')+'\n')