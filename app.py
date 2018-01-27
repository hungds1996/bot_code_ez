# from flask import Flask, render_template, redirect, url_for
# from pymongo import *
# from bot import Steam_guard_code
# from backup_code import *
#
# app = Flask(__name__)
#
# client = MongoClient('mongodb://admin:admin@ds137826.mlab.com:37826/ezgame')
# db = client.get_default_database()
#
# bot_data = db.Steam_guard_code
#
# @app.route('/')
# def bot():
#     bot_list = bot_data.find()
#     return render_template('bot.html', bots=bot_list)
#
# @app.route('/<id>')
# def update(id):
#     picked_bot = bot_data.find_one({"bot_id": id})
#     new_code = picked_bot['code']
#     new_code.pop(0)
#     bot_data.update_one({'bot_id':id}, {"$set": {'code':new_code}}, upsert=False)
#     back_up(picked_bot['bot_id'])
#     return redirect(url_for('bot'))
#
# if __name__ == '__main__':
#   app.run(debug=True)


from flask import Flask, render_template, redirect, url_for
from pymongo import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from report import *
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://admin:admin@ds137826.mlab.com:37826/ezgame')
db = client.get_default_database()

bot_data = db.Steam_guard_code
chrome_options = Options()
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
def back_up(target):
    bot_list = bot_data.find()

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

@app.route('/')
def bot():
    bot_list = bot_data.find()
    return render_template('bot.html', bots=bot_list)

@app.route('/<id>')
def update(id):
    picked_bot = bot_data.find_one({"bot_id": id})
    new_code = picked_bot['code']
    new_code.pop(0)
    bot_data.update_one({'bot_id':id}, {"$set": {'code':new_code}}, upsert=False)
    back_up(picked_bot['bot_id'])
    return redirect(url_for('bot'))

if __name__ == '__main__':
  app.run(debug=True)
