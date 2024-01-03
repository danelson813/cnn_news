from selenium import webdriver
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from time import sleep
from .util import setup_logger
import pandas as pd


def get_soup(url_):
    logger = setup_logger()
    options = Options()
    options.add_argument('--headless')
    ua = UserAgent()
    user_agent = ua.random
    logger.critical(f"{user_agent}")
    options.add_argument(f'user-agent:{user_agent}')
    with webdriver.Firefox(service=Service('/Users/geckodriver'), options=options) as driver:
        driver.get(url_)
        sleep(2)
        driver.maximize_window()
        driver.save_screenshot("data/homepage.png")
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        return soup
    
def save_soup(soup):
    with open('data/soup_cnn.txt', 'w') as f:
        f.write(soup)

def retreive_soup(filename):
    with open(filename, 'r') as f:
        text = f.read()
        return BeautifulSoup(text, 'html.parser')