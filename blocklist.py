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
            if i == 600:
                scroll = False
            i += 1
            print(i)

class Block:
    def __init__(self, soup: BeautifulSoup) -> None:
        self.soup = soup
        self._parse_data()

    def _parse_data(self):
        """Parse the data from the row"""
        row_items = self.soup.findAll("td")
        self.height = int(row_items[0].text)
        self.maturity = row_items[1].text
        self.difficulty = row_items[2].text
        self.block_hash = row_items[3].text
        self.time_found = row_items[4].text
        self.luck = row_items[5].text
        self.reward = row_items[6].text

# if __name__ == "__main__":
#     blocklist = BlockList("https://web.xmrpool.eu/xmr-pool-blocks.html")

