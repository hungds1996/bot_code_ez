from flask import Flask, render_template, redirect, url_for
from pymongo import *
from bot import Steam_guard_code
app = Flask(__name__)

client = MongoClient('mongodb://admin:admin@ds137826.mlab.com:37826/ezgame')
db = client.get_default_database()

bot_data = db.Steam_guard_code

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
    return redirect(url_for('bot'))

if __name__ == '__main__':
  app.run(debug=True)
