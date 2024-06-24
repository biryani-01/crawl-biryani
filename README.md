# crawl-biryani

`crawl-biryani` is a Python script designed to deeply crawl websites. It reads multiple URLs from a `urls.txt` file, crawls each URL to a specified depth, and saves the results in a user-specified `.txt` file. The script features a creepy green banner and verbose crawling output.

## Features
- Reads multiple URLs from `urls.txt`
- Crawls websites deeply, extracting all links
- Allows specification of maximum crawling depth
- Verbose output displaying the current URL being crawled
- Saves results in a user-specified `.txt` file
- Creepy green banner with the text "crawl-biryani"

## Requirements
- Python 3.x
- `requests` library
- `urllib.parse` library
- `BeautifulSoup` from `bs4` library
- `termcolor` library
- `pyfiglet` library

## Installation
1. Clone the repository or download the script.
2. Install the required Python libraries:
    ```sh
    pip install requests beautifulsoup4 termcolor pyfiglet
    ```

## Usage
1. Create a file named `urls.txt` and add the list of URLs to crawl, each on a new line.
2. Run the script:
    ```sh
    python crawl_biryani.py
    ```
3. Follow the prompts:
    - Enter the path to the `urls.txt` file.
    - Enter the path for the results file (e.g., `results.txt`).
    - Enter the maximum depth for crawling.

## Example
```plaintext
$ python crawl_biryani.py
