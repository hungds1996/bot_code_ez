import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from report import *
from pymongo import MongoClient

def back_up(target):
    client = MongoClient('mongodb://admin:admin@ds137826.mlab.com:37826/ezgame')
    db = client.get_default_database()
    bot_data = db.Steam_guard_code
    bot_list = bot_data.find()

    # code_list.update_one({
    #     'bot_id' : 'Ezgamebot79'
    # },{
    #     '$set' : {
    #     'code' : ['XFF8Y32', '9QNFN42', '4P98B36']
    #     }
    # })
    for bot in list(bot_list):
        bot_id = bot['bot_id']
        bot_pass = bot['bot_pass']
        codes = bot['code']
        if bot_id == target:
            login(bot_id, bot_pass, codes[0])
            timeout = 100
            click('''//*[@id="account_pulldown"]''')
            click('''//*[@id="account_dropdown"]/div/a[2]''')
            click('''//*[@id="main_content"]/div[2]/div[6]/div[1]/div[2]/div[1]/a''')
            click('''//*[@id="steam_authenticator_emergency_codes"]/div/div[3]/button''')
            submit('''/html/body/div[3]/div/div/form/div/input''', codes[1])
            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="twofactor_printable"]''')))
            code1 = browser.find_elements_by_class_name('twofactor_emergency_code_left')
            code2 = browser.find_elements_by_class_name('twofactor_emergency_code')
            codes = code1 + code2
            guard_code_list = []
            for code in codes:
                guard_code = code.text
                guard_code_list.append(guard_code)

            bot_data.update_one({
                'bot_id' :  bot_id
            },{
                '$set' : {
                'code' : guard_code_list
                }
            })
            logout()
