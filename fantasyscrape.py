import requests
from bs4 import BeautifulSoup
from itertools import cycle
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random

headers = {
    'Host': 'www.google.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
}

# Enter proxy IP addresses and ports in a list.
proxies = [
'http://194.163.175.163:3128',  
'http://210.75.50.242:9002',  
'http://45.167.124.154:999',
'http://178.154.212.6:3128',
"http://47.97.97.119:3128",
"http://41.76.145.18:8080",
"http://36.95.249.157:8080",
"http://190.121.207.183:999",
"http://186.97.172.178:60080",
"http://188.43.247.36:3128",
"http://150.136.4.250:3128",
"http://167.71.225.180:3128",
"http://43.130.148.94:80",
"http://185.191.236.162:3128"
]

proxy_pool = cycle(proxies)

def qbs():
    random.shuffle(proxies)
    # Initialize a URL.
    url = 'https://httpbin.org/ip'

    file = open("qbs.txt", "w")

    # Iterate through the proxies and check if they are working.
    for i in range(1, len(proxies)):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=30)
            print(response.json())

            # Set path to chromedriver executable
            webdriver_service = Service('/path/to/chromedriver')  # Replace with the correct path

            # Configure Chrome options
            chrome_options = Options()
            chrome_options.add_argument('Host: www.google.com')
            chrome_options.add_argument('User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36')

            # Create a new instance of the Chrome driver
            driver = webdriver.Chrome(service=webdriver_service)

            # Load the webpage
            driver.get('https://www.fantasypros.com/nfl/rankings/qb.php')

            # Find the table rows
            rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
            result = driver.page_source
            soup = BeautifulSoup(result, 'html.parser')
            page =  soup.findAll('td', class_="")
            limit=0 #player limit
            player=0 #creates gap

            print("1")
            for i in page:
                if limit<96:
                    limit=limit+1
                    
                    if player==3:
                        print("")
                        print(int(limit/3+1))
                        player=0
                        
                    print(i.text)
                    file.write(f"{i.text}\n")
                    player=player+1

                        
                else:
                    break

            # Quit the browser
            driver.quit()
            break

        except requests.exceptions.RequestException as e:
            print("Skipping. Connection error")
            print(traceback.format_exc())
 
def wrs():
    random.shuffle(proxies)
    # Initialize a URL.
    url = 'https://httpbin.org/ip'

    file = open("wrs.txt", "w")

    # Iterate through the proxies and check if they are working.
    for i in range(1, 5):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=30)
            print(response.json())

            # Set path to chromedriver executable
            webdriver_service = Service('/path/to/chromedriver')  # Replace with the correct path

                    # Configure Chrome options
            chrome_options = Options()
            chrome_options.add_argument('Host: www.google.com')
            chrome_options.add_argument('User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

            # Create a new instance of the Chrome driver
            driver = webdriver.Chrome(service=webdriver_service)

            # Load the webpage
            driver.get('https://www.fantasypros.com/nfl/rankings/wr.php')

            # Find the table rows
            rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
            result = driver.page_source
            soup = BeautifulSoup(result, 'html.parser')
            page =  soup.findAll('td', class_="")
            limit=0 #player limit
            player=0 #creates gap

            
            for i in page:
                if limit<150:
                    limit=limit+1
                    
                    if player==3:
                        print("")
                        print(int(limit/3+1))
                        player=0
                    print(i.text)
                    file.write(f"{i.text}\n")
                    player=player+1

                        
                else:
                    break

            # Quit the browser
            driver.quit()
            break

        except requests.exceptions.RequestException as e:
            print("Skipping. Connection error")
            print(traceback.format_exc())

def rbs():
    random.shuffle(proxies)
    # Initialize a URL.
    url = 'https://httpbin.org/ip'

    file = open("rbs.txt", "w")

    # Iterate through the proxies and check if they are working.
    for i in range(1, 5):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=30)
            print(response.json())

            # Set path to chromedriver executable
            webdriver_service = Service('/path/to/chromedriver')  # Replace with the correct path

                    # Configure Chrome options
            chrome_options = Options()
            chrome_options.add_argument('Host: www.google.com')
            chrome_options.add_argument('User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

            # Create a new instance of the Chrome driver
            driver = webdriver.Chrome(service=webdriver_service)

            # Load the webpage
            driver.get('https://www.fantasypros.com/nfl/rankings/rb.php')

            # Find the table rows
            rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
            result = driver.page_source
            soup = BeautifulSoup(result, 'html.parser')
            page =  soup.findAll('td', class_="")
            limit=0 #player limit
            player=0 #creates gap

            
            for i in page:
                if limit<150:
                    limit=limit+1
                    
                    if player==3:
                        print("")
                        print(int(limit/3+1))
                        player=0
                        
                    print(i.text)
                    file.write(f"{i.text}\n")
                    player=player+1

                        
                else:
                    break

            # Quit the browser
            driver.quit()
            break

        except requests.exceptions.RequestException as e:
            print("Skipping. Connection error")
            print(traceback.format_exc())

def te():
    random.shuffle(proxies)
    # Initialize a URL.
    url = 'https://httpbin.org/ip'

    file = open("tes.txt", "w")

    # Iterate through the proxies and check if they are working.
    for i in range(1, 5):
        # Get a proxy from the pool
        proxy = next(proxy_pool)
        print("Request #%d" % i)
        try:
            response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=30)
            print(response.json())

            # Set path to chromedriver executable
            webdriver_service = Service('/path/to/chromedriver')  # Replace with the correct path

                    # Configure Chrome options
            chrome_options = Options()
            chrome_options.add_argument('Host: www.google.com')
            chrome_options.add_argument('User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')

            # Create a new instance of the Chrome driver
            driver = webdriver.Chrome(service=webdriver_service)

            # Load the webpage
            driver.get('https://www.fantasypros.com/nfl/rankings/te.php')

            # Find the table rows
            rows = driver.find_elements(By.CSS_SELECTOR, 'tbody tr')
            result = driver.page_source
            soup = BeautifulSoup(result, 'html.parser')
            page =  soup.findAll('td', class_="")
            limit=0 #player limit
            player=0 #creates gap

            
            for i in page:
                if limit<150:
                    limit=limit+1
                    
                    if player==2:
                        print("")
                        print(int(limit/3))
                        player=0
                        
                    print(i.text)
                    file.write(f"{i.text}\n")
                    player=player+1

                        
                else:
                    break

            # Quit the browser
            driver.quit()
            break

        except requests.exceptions.RequestException as e:
            print("Skipping. Connection error")
            print(traceback.format_exc())

def calc_rb():
    None
    #convert stats to int
    #compare stats through algorithm
    
def calc_wr():
    None
    #convert stats to int
    #compare stats through algorithm
    
def calc_qb():
    None
    #convert stats to int
    #compare stats through algorithm

if __name__ == "__main__":
    print("Running backs")
    rbs()

    time.sleep(6)#various time increments to avoid suspision

    print("Wide Recivers")
    print("")
    wrs()

    time.sleep(9)

    print("Quaterbacks")
    print("")
    qbs()

    time.sleep(4)

    te()

    
