import os
import time

from selenium.webdriver import Chrome
from bs4 import BeautifulSoup

CHROMEDRIVER = os.path.abspath("../chromedriver.exe")

class BlockList:
    def __init__(self, url: str):
        self.url = url

        self.chrome = Chrome(executable_path=CHROMEDRIVER)
        self.chrome.get(self.url)

        self._load_all_blocks()

    def _load_all_blocks(self):
        """Load list of Block instances"""
        self.table = self.chrome.find_element_by_class_name("table")
        self.blocks = []
        scroll = True

        # Scroll to the bottom
        i = 0
        while scroll:
            time.sleep(.3)
            self.load_button = self.chrome.find_element_by_id("loadMoreBlocks")
            self.load_button.click()
            if i == 1000:
                scroll = False
            i += 1
            print(i)

class Block:
    def __init__(self, soup: BeautifulSoup) -> None:
        pass

if __name__ == "__main__":
    blocklist = BlockList("https://web.xmrpool.eu/xmr-pool-blocks.html")

