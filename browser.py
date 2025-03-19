from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import selenium

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument("blink-settings=imagesEnabled=false")
chrome_options.add_argument("--user-data-dir=/home/wxt/.chrome-generals")

driver = webdriver.Chrome(
        service=Service('./result/bin/chromedriver'),
        options=chrome_options)

driver.get("https://generals.io")
driver.get("https://generals.io/replays/eOzEsKuZd?p=wxt1221")

time.sleep(1)

next_step = driver.find_element(
        By.XPATH,
        "//*[@id=\"replay-bottom-bar\"]/div[3]/span")

mapall = []
endall = 1
ii = ""
while endall:
    i = 1
    j = 0
    end1 = 1
    map = []
    while end1:
        curj = 0
        end2 = 1
        maptemp = []
        try:
            element = driver.find_element(
                    By.CSS_SELECTOR,
                    f"#gameMap > tbody > tr:nth-child({i})")
        except selenium.common.exceptions.NoSuchElementException:
            end1 = 0
        else:
            while end2:
                curj = curj + 1
                try:
                    element = driver.find_element(
                            By.CSS_SELECTOR,
                            f"#gameMap > tbody > tr:nth-child({i}) > td:nth-child({curj})")  # noqa: E501
                except selenium.common.exceptions.NoSuchElementException:
                    end2 = 0
                else:
                    maptemp.append(
                            [element.get_attribute("class"),
                             element.text])
            map.append(maptemp)
            j = curj
            i = i + 1
    i = i - 1
    j = j - 1
    next_step.click()
    element = driver.find_element(By.XPATH, "//*[@id=\"turn-counter\"]")
    if ii == element.text:
        endall = 0
    else:
        ii = element.text
        print("Down "+ii)
        mapall.append(map)
        print(map)
driver.quit()
