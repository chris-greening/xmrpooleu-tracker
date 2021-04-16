import os

from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

CHROMEDRIVER = os.path.abspath("../chromedriver.exe")

class BlockList:
    def __init__(self, url: str):
        self.url = url

        self.chrome = Chrome(executable_path=CHROMEDRIVER)
        self.chrome.get(self.url)


if __name__ == "__main__":
    blocklist = BlockList("https://web.xmrpool.eu/xmr-pool-blocks.html")

