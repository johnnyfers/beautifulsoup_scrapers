import os
from selenium import webdriver
import undetected_chromedriver
from pyvirtualdisplay import Display


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = undetected_chromedriver.Chrome(options)
    
    return driver


