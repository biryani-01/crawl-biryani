import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
from termcolor import colored
import pyfiglet

def crawl(url, max_depth, visited, result_file):
    if max_depth <= 0 or url in visited:
        return
    print(f"Crawling: {url}")
    visited.add(url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(result_file, 'a') as file:
                file.write(f"{url}\n")
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', href=True):
                next_url = urljoin(url, link['href'])
                if urlparse(next_url).netloc == urlparse(url).netloc:
                    crawl(next_url, max_depth - 1, visited, result_file)
    except requests.exceptions.RequestException as e:
        print(f"Error crawling {url}: {e}")

def main():
    # Display the banner
    banner = pyfiglet.figlet_format("crawl-biryani")
    print(colored(banner, 'green'))

    urls_file = input("Enter the path to the urls.txt file: ")
    result_file = input("Enter the path for the results to be saved (e.g., results.txt): ")
    max_depth = int(input("Enter the maximum depth to crawl: "))

    # Ensure the result file is empty before starting
    open(result_file, 'w').close()

    with open(urls_file, 'r') as file:
        urls = file.readlines()
        visited = set()
        for url in urls:
            url = url.strip()
            if url:
                crawl(url, max_depth, visited, result_file)

    print(f"Results saved in {result_file}")

if __name__ == "__main__":
    main()
