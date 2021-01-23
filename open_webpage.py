import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def open_video_stream(video_id):
    # old chrome options (from testing, chrome + extensions seems less stable than ff + extensions)
    # chrome_options = Options()
    # chrome_options.add_experimental_option("detach", True)
    # chrome_options.add_argument("--headless")
    # chrome_options.add_extension('extension_1_29_2_0.crx')
    # chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    # driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), options=chrome_options)

    # old firefox tests
    # binary = FirefoxBinary(os.path.abspath('C:\Program Files\Mozilla Firefox\Firefox.exe'))
    # driver = webdriver.Firefox(firefox_binary=binary, executable_path=os.path.abspath("geckodriver"))

    # set current ff options
    # profile = webdriver.FirefoxProfile()
    firefox_options = webdriver.FirefoxOptions()
    # profile.set_preference("javascript.enabled", True)
    firefox_options.add_argument("--headless")
    driver = webdriver.Firefox(executable_path=os.path.abspath("geckodriver"), firefox_options=firefox_options)

    # install uBlock origin to block YT preroll ads from being transcripted
    driver.install_addon(os.path.abspath('uBlock0@raymondhill.net.xpi'), temporary=True)

    # grab the video in question
    driver.get("https://www.youtube.com/watch?v={0}".format(video_id))
    

    # set a delay just in case -- sometimes the page can be a bit slow to load, depending on allotted resources of host
    delay = 60  # in seconds
    try:
        my_elem = WebDriverWait(driver, delay).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@class='ytp-large-play-button ytp-button']")))
        print("Page is ready!")
    except Exception as e:
        print(e)

    # print(driver.page_source.encode("utf-8"))

    # look for the play button, because videos do not always autoplay

    element = driver.find_element_by_xpath("//*[@class='ytp-large-play-button ytp-button']")
    # element = driver.find_element_by_id("player-container")
    element.click()
    # driver.send_keys("K")
    try:
        # driver.execute_script("arguments[0].click();", element)
        # my_elem.send_keys("K")
        print("I clicked it!")


    except Exception as e:
        print(e)
        pass

    # loop to exit the script in case of autoplaying next video
    old_page = str(driver.current_url)

    while True:
        time.sleep(10)
        if old_page != str(driver.current_url):
            print('Page change detected')
            os._exit(1)

            return False

