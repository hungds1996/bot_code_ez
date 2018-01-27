import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from pymongo import MongoClient
import pyexcel

def login(bot_id, bot_pass, guard_code):
    timeout = 100
    try:
        browser.get('https://store.steampowered.com//login/?redir=app%2F359550%2FTom_Clancys_Rainbow_Six_Siege%2F')
        pass_box = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="input_password"]''')))
        id_box = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="input_username"]''')))
        btn = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="login_btn_signin"]/button''')))
        id_box.send_keys(bot_id)
        pass_box.send_keys(bot_pass)
        pass_box.submit()
        code = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="twofactorcode_entry"]''')))
        code.send_keys(guard_code)
        code.submit()
    except TimeoutException:
        print('timeout')

def balance(target):
    timeout = 100
    try:
        steam = WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, target)))
        balances = browser.find_element_by_xpath(target)
        return(balances.text)
    except TimeoutException:
        print('timeout')

def logout():
    timeout = 100
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="account_pulldown"]''')))
        view = browser.find_element_by_xpath('''//*[@id="account_pulldown"]''').click()
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, '''//*[@id="account_dropdown"]/div/a[1]''')))
        logout = browser.find_element_by_xpath('''//*[@id="account_dropdown"]/div/a[1]''').click()
    except TimeoutException:
        pritn('timeout')

def click(target):
    timeout = 100
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, target)))
        view = browser.find_element_by_xpath(target).click()
    except TimeoutException:
        pass

def submit(target, value):
    timeout = 100
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, target))).send_keys(value)
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, target))).submit()

browser = webdriver.Chrome(executable_path="D:\C4E\EZ\page\chromedriver.exe")
# client = MongoClient('mongodb://admin:admin@ds137826.mlab.com:37826/ezgame')
# db = client.get_default_database()
#
# balances = []
#
# bot_data = db.Steam_guard_code
# bot_list = bot_data.find()
#
# for bot in bot_list:
#     bot_id = bot['bot_id']
#     bot_pass = bot['bot_pass']
#     codes = bot['code']
#
#     get = login(bot_id, bot_pass, codes[0])
#     codes.pop(0)
#     bot_data.update_one({
#         'bot_id' :  bot_id
#     },{
#         '$set' : {
#         'code' : codes
#         }
#     })
#
#     if '₫' in balance('''//*[@id="header_wallet_balance"]'''):
#         balance_final = balance('''//*[@id="header_wallet_balance"]''').replace('.', '').replace(',', '.').replace('₫', '')
#     elif "Rp" in balance('''//*[@id="header_wallet_balance"]'''):
#         balance_final = balance('''//*[@id="header_wallet_balance"]''').replace(' ', '').replace('Rp', '')
#
#     browser.get('http://steamcommunity.com/market/')
#     market_final = balance('''//*[@id="totalRow0"]/div[1]/span/span[2]''').replace('(Rp ', '').replace(')', '')
#
#     bot_balance = {
#         'bot' : bot_id,
#         'balance' : balance_final,
#         'market' : market_final
#     }
#
#     balances.append(bot_balance)
#     print(balances)
#     logout()
#
# pyexcel.save_as(records=balances, dest_file_name='report.xlsx')
