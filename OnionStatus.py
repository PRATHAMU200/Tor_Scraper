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


# Tor checking if link up or not
def check_link(url):
	global up,down
	session = get_tor_session()
	if (url[:7]!="http://") & (url[:8]!="https://"):
		url = "https://"+url
	try:
		reqs = session.get(url)
		r = reqs.status_code
		if r==200:
			up+=1
			soup = BeautifulSoup(reqs.text, 'html.parser')
			title = (soup.find('title')).string
			print(Fore.GREEN+url+" : "+title)
			print(Style.RESET_ALL)
		elif r==404:
			down+=1
			print(Fore.MAGENTA+url+" ....Down...")
			print(Style.RESET_ALL)
		else:
			print(Fore.YELLOW+url+" ...."+str(r))
			print(Style.RESET_ALL)
	except:
		down+=1
		print(Fore.RED+url+' ....Down')
		print(Style.RESET_ALL)

def check_links(links, num_threads):
    # Create a thread for each link
    threads = []
    for i in links:
    	try:
    		t = threading.Thread(target=check_link, args=(i.strip(),))
    		threads.append(t)
    		t.start()
    		while threading.active_count() >= num_threads:
    			pass
    	except:
    		print(Fore.RED+"Exception occur in this thread")
        
    # Wait for all threads to finish
    for t in threads:
        t.join()


#Checking all up/down onion links from list of links
if "-F" in sys.argv:
	file = sys.argv[sys.argv.index("-F")+1]
	num_threads = 10  # Default number of threads
	if "-T" in sys.argv:
		num_threads = int(sys.argv[sys.argv.index("-T")+1])
	with open(file , "r") as f:
		links = f.readlines()
		up,down,total = 0,0,len(links)
		check_links(links, num_threads)
		print(Fore.YELLOW+"Total:"+str(total)+"    "+Fore.GREEN+"Up:"+str(up)+"    "+Fore.RED+"Down:"+str(down))
		print(Style.RESET_ALL)
		# for i in links:
		# 	try:
		# 		print(check_links(i.strip(),num_threads))
		# 		print(Style.RESET_ALL)
		# 	except:
		# 		print(Fore.MAGENTA+i.strip()+' NOT Able to connect to server')
		# 		print(Style.RESET_ALL)


else:
	print('''
	TORSCRAPER: This is a WebScraping tool having different functions.

		-H       :   help
		-F file  :   file name to check if links are up or not
		-T num   :   Number of threads to use[Default: 10]

	Example:
		python torscraper.py -F links.txt
		python torscraper.py -F links.txt -T 20''')
print(Style.RESET_ALL)