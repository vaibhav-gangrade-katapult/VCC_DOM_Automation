from random import randint
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver

from BaseFunctions.find_locator import findby_XPATH, wait_for_element, findby_Class, findby_ID, findby_CSS, \
    find_by_elements
from BaseFunctions.loadObjFile import config_parser
from FunctionalMethods.driverSetup import getWebDriver
from BaseFunctions.find_locator import srollTo

config = config_parser()


class TestIKEA:
    def setup_driver(self):
        drv = getWebDriver()
        drv.refresh()
        drv.maximize_window()
        drv.get(config['retailer_url']['IKEAurl'])
        return drv

    def add_to_bag(self):
        drv = myobj.setup_driver()
        add_to_bag_btn = findby_XPATH(drv, config['IKEA']['add_to_bag_xpath'])
        srollTo(drv, add_to_bag_btn)
        add_to_bag_btn.click()
        sleep(randint(2, 5))
        # wait_for_element(drv, By.XPATH, config['IKEA']['link_text_xpath'])
        # contn_to_bag_link = findby_XPATH(drv, config['IKEA']['link_text_xpath'])
        # contn_to_bag_link.click()
        drv.refresh()
        wait_for_element(drv, By.CLASS_NAME, config['IKEA']['cart_icon_class'])
        cart_icon = findby_Class(drv, config['IKEA']['cart_icon_class'])
        cart_icon.click()
        sleep(randint(2, 5))
        return drv

    def procced_to_shipping(self):
        drv = myobj.add_to_bag()
        wait_for_element(drv, By.XPATH, config['IKEA']['enter_zip_code_link_xpath'])
        zip_update_link = findby_XPATH(drv, config['IKEA']['enter_zip_code_link_xpath'])
        zip_update_link.click()
        wait_for_element(drv, By.XPATH, config['IKEA']['zip_text_box_xpath'])
        zip_field = findby_XPATH(drv, config['IKEA']['zip_text_box_xpath'])
        zip_field.click()
        zip_field.send_keys(config['userDetail']['zip'])
        zip_btn = findby_Class(drv, config['IKEA']['zip_update_btn_class'])
        zip_btn.click()
        sleep(randint(2, 5))
        # wait_for_element(drv, By.XPATH, config['IKEA']['deliver_option_xpath'])
        delivery_option = findby_XPATH(drv, config['IKEA']['deliver_option_xpath'])
        delivery_option.click()
        continue_to_checkout = findby_Class(drv, config['IKEA']['cont_to_checkout_class'])
        # srollTo(drv, continue_to_checkout)
        continue_to_checkout.click()
        drv.find_element(By.CLASS_NAME, 'cart-ingka-modal-header').click()
        sleep(randint(2, 4))
        guestbtn = find_by_elements(drv, By.CSS_SELECTOR, config['IKEA']['guest_checkout_btn_css'])
        sleep(randint(2, 5))
        list_gst = len(guestbtn)
        print(list_gst)
        for i in range(0, list_gst):
            if guestbtn[i].text == 'Guest checkout':
                print(i)
                print(guestbtn[i].text)
                guestbtn[i].click()
                print('vab')
        sleep(randint(10, 15))

        wait_for_element(drv, By.XPATH, config['IKEA']['cont_btn_xpath'])
        cont_btn = findby_XPATH(drv, config['IKEA']['cont_btn_xpath'])
        srollTo(drv, cont_btn)
        sleep(randint(2, 5))
        cont_btn.click()
        sleep(randint(2, 5))
        return drv

    def add_shipping_detail(self):
        drv = myobj.procced_to_shipping()
        print("welcome to shipping page")
        drv.refresh()
        zip_address_filled = findby_Class(drv, config['IKEA']['zip_filled_class'])
        srollTo(drv, zip_address_filled)
        sleep(randint(3, 7))

        # wait_for_element(drv, By.ID, config['IKEA']['first_name_id'])
        # f_name = findby_CSS(drv, config['IKEA']['first_name_css'])
        # f_name.send_keys(config['userDetail']['first_name'])

        f_name = findby_ID(drv, config['IKEA']['first_name_id'])
        f_name.click()
        f_name.send_keys(config['userDetail']['first_name'])
        l_name = findby_ID(drv, config['IKEA']['last_name_id'])
        l_name.click()
        l_name.send_keys(config['userDetail']['last_name'])
        address1 = findby_XPATH(drv, config['IKEA']['address_xpath'])
        address1.click()
        address1.send_keys(config['userDetail']['addressLine1'])
        sleep(randint(2, 3))
        cont_btn_ship = findby_XPATH(drv, config['IKEA']['cont_btn_ship_xpath'])
        srollTo(drv, cont_btn_ship)
        sleep(randint(4, 7))
        email_ship = findby_ID(drv, config['IKEA']['email-id'])
        email_ship.click()
        email_ship.send_keys(config['userDetail']['email'])
        mobile = findby_ID(drv, config['IKEA']['phone_id'])
        mobile.click()
        mobile.send_keys(config['userDetail']['phone'])
        sleep(randint(2, 3))
        click_to_check = findby_Class(drv, config['IKEA']['IKEA_family_class'])
        click_to_check.click()
        cont_btn_ship.click()
        sleep(randint(2, 5))
        return drv

    def verify_details(self):
        drv = myobj.add_shipping_detail()
        print("welcome to verify user details page")
        wait_for_element(drv, By.CLASS_NAME, config['IKEA']['verify_addr_alert_class'])
        my_add_btn = findby_CSS(drv, config['IKEA']['verify_add_css'])
        my_add_btn.click()
        sleep(randint(2, 5))
        wait_for_element(drv, By.CSS_SELECTOR, config['IKEA']['where_del_text_css'])
        house_opt = findby_XPATH(drv, config['IKEA']['house_opt_xpath'])
        house_opt.click()
        no_opt = findby_XPATH(drv, config['IKEA']['no_opt_xpath'])
        no_opt.click()
        save_add_btn = findby_CSS(drv, config['IKEA']['save_ans_css'])
        save_add_btn.click()
        sleep(randint(3, 5))
        wait_for_element(drv, By.XPATH, config['IKEA']['your_details_xpath'])
        get_text_ele = findby_CSS(drv, config['IKEA']['your_detail_text_css'])
        save_text = get_text_ele.text

        comma_list = save_text.split('\n')
        print(comma_list)
        # var0 = comma_list[0] in 'Vaibhav'
        # print(var0)

        assert comma_list[0] == config['userDetail']['first_name']+' '+config['userDetail']['last_name']
        assert comma_list[1] == config['userDetail']['addressLine1']
        assert comma_list[2] == config['userDetail']['city']+', '+config['userDetail']['state']+' '+config['userDetail']['zip']
        assert comma_list[3] == config['userDetail']['state']
        assert comma_list[4] == config['userDetail']['email']
        assert comma_list[5] == '+1'+config['userDetail']['phone']


myobj = TestIKEA()
myobj.verify_details()
