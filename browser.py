from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument("blink-settings=imagesEnabled=false")
chrome_options.add_argument("--user-data-dir=/home/wxt/.chrome-generals")
chrome_options.set_capability('pageLoadStrategy', 'eager')

driver = webdriver.Chrome(
        service=Service('./result/bin/chromedriver'),
        options=chrome_options)

driver.get("https://generals.io")
driver.get("https://generals.io/replays/eOzEsKuZd?p=wxt1221")
print("Get the Page!")

next_step = driver.find_element(
        By.XPATH,
        "//*[@id=\"replay-bottom-bar\"]/div[3]/span")

mapall = []
endall = 1
ii = ""
cnt = 0
element_all = driver.find_element(
                    By.XPATH,
                    "/html/body/div/div/div/div[2]/table/tbody")
element_all = element_all.find_elements(
                    By.XPATH,
                    "./*")
turn = driver.find_element(By.XPATH, "//*[@id=\"turn-counter\"]")
map = []
for iii in element_all:
    maptemp = []
    element_hang = iii.find_elements(
                    By.XPATH,
                    "./*")
    map.append(element_hang)
i = len(map)
j = len(map[0])
while endall:
    mapcur = (driver.execute_script("""
    let list = [];
    for(var i=0;i<arguments[0].length;i++){
        let list2 = [];
        for(var j=0;j<arguments[0][i].length;j++){
            let list3 = [];
            list3.push(arguments[0][i][j].innerText);
            list3.push(arguments[0][i][j].className);
            list2.push(list3);
        }
        list.push(list2)
    }
    return list;""", map))
    begin_time = time.time()
    next_step.click()
    end_time = time.time()
    print(end_time-begin_time)
    if ii == turn.text:
        endall = 0
    ii = turn.text
    print("Down "+ii)
    mapall.append(mapcur)
driver.quit()
