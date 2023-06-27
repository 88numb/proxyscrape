import requests
from bs4 import BeautifulSoup
from datetime import datetime

# List of URLs for proxy scraping
urls = [
    "http://www.proxyserverlist24.top/feeds/posts/default",
    "http://proxyape.com/",
    "http://sslproxies24.blogspot.in/feeds/posts/default",
    "https://proxyunique.com",
    "http://rootjazz.com/proxies/proxies.txt",
    "http://www.live-socks.net/feeds/posts/default",
    "http://www.httptunnel.ge/ProxyListForFree.aspx",
    "https://hidemy.name/en/proxy-list/",
    "https://free-proxy-list.net/",
    "https://www.proxynova.com/",
    "http://www.proxylists.net/",
    "http://www.freeproxylists.net/",
    "http://Gatherproxy.com",
    "http://free-proxy.cz/en/",
    "http://spys.one/en/"
]

# Function to scrape proxies from a URL
def scrape_proxies(url):
    proxies = []
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        proxy_tags = soup.find_all("tr")
        for tag in proxy_tags:
            proxy = tag.get_text().strip()
            if proxy:
                proxies.append(proxy)
    except requests.exceptions.RequestException:
        pass
    return proxies

# Function to save proxies to a text file
def save_proxies(proxies, filename):
    with open(filename, "w") as file:
        file.write("\n".join(proxies))

# Main program
all_proxies = []
for url in urls:
    proxies = scrape_proxies(url)
    all_proxies.extend(proxies)

# Format date and time
now = datetime.now()
timestamp = now.strftime("%Y%m%d/%H:%M")

# File name to save the proxy list
output_file = f"proxies_{timestamp}.txt"

save_proxies(all_proxies, output_file)
print("The list of working proxies has been saved in", output_file)
