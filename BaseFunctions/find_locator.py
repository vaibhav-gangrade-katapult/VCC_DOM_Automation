
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def findby_XPATH(drv, loc):
    ele = drv.find_element(By.XPATH, loc)
    return ele


def findby_Class(drv, loc):
    ele = drv.find_element(By.CLASS_NAME, loc)
    return ele


def findby_ID(drv, loc):
    ele = drv.find_element(By.ID, loc)
    return ele


def findby_linkText(drv, loc):
    ele = drv.find_element(By.LINK_TEXT, loc)
    return ele


def findby_CSS(drv, loc):
    ele = drv.find_element(By.CSS_SELECTOR, loc)
    return ele


def wait_for_element(drv, bytype, loc):
    try:
        element = WebDriverWait(drv, 12).until(
            EC.presence_of_element_located((bytype, loc))
        )
    finally:
        print("no such element")
    return element


def find_by_elements(drv, bytype, loc):
    ele = drv.find_elements(bytype, loc)
    return ele


def srollTo(drv, ele_loc):
    drv.execute_script("arguments[0].scrollIntoView();", ele_loc)
