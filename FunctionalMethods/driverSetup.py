import codecs
# import time
from random import randint
from time import sleep

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium_stealth import stealth

from BaseFunctions.loadObjFile import config_parser

config = config_parser()


def getWebDriver():
    serv = Service(config['filePath']['chromeDriver'])
    # Avoiding detection
    options = Options()
    # Screen resolution set to minimum, maximize screen is one of pattern identified by the bot
    options.add_argument("window-size=1536,664")
    # Chrome is controlled by automated test software
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument('--disable-gpu')
    # Initiate user agent with webdeiver
    user_agent = UserAgent()
    user_agent = user_agent.random
    print(user_agent)
    options.add_argument(f'user-agent={user_agent}')
    # options.add_argument(
    #     '--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) '
    #     'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.74 Mobile Safari/537.36 Edge/12.10166"')
    driver = webdriver.Chrome(service=serv, options=options)
    # Selenium Stealth settings
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    return driver


# def run_driver(url):
#     drv = getWebDriver()
#     drv.refresh()
#     drv.maximize_window()
#     # drv.delete_all_cookies()
#     sleep(randint(2, 7))
#     # driver.delete_network_conditions()
#     drv.get(url)
#     return drv
#
#     # get_url_link = getURL_List()
#     # for i in range(0, len(get_url_link)):
#         # drv = getWebDriver()
#         # drv.refresh()
#         # drv.maximize_window()
#         # # drv.delete_all_cookies()
#         # sleep(randint(2, 7))
#         # # driver.delete_network_conditions()
#         # drv.get(get_url_link[i])
#         # sleep(randint(2, 7))
#         # ff = open(config['filePath']['html_file_name'] + str(i) + '.html', 'w')
#         # ff.close()
#         # sleep(randint(2, 7))
#         # # open file in write mode with encoding
#         # f = codecs.open(config['filePath']['html_file_name'] + str(i) + '.html', "r+", "utf8")
#         # # obtain page source
#         # h = drv.page_source
#         # # write page source content to file
#         # f.write(h)
#         # sleep(randint(2, 7))
#         # print("Page " + str(i + 1) + " Saved")
#         # drv.close()
#         # sleep(randint(2, 7))
