from flask import Flask, render_template
from pymongo import *
from bot import Steam_guard_code
app = Flask(__name__)

@app.route('/<id>')
def bot(id):
    client = MongoClient('mongodb://admin:admin@ds137826.mlab.com:37826/ezgame')
    db = client.get_default_database()

    bot_data = db.Steam_guard_code
    bot_list = bot_data.find()
    if id == "0":
        return render_template('bot.html', bots=bot_list)
    else:
        picked_bot = bot_data.find_one({"bot_id": id})
        new_code = picked_bot['code']
        new_code.pop(0)
        bot_data.update_one({'bot_id':id}, {"$set": {'code':new_code}}, upsert=False)
        return render_template('bot.html', bots=bot_list)

if __name__ == '__main__':
  app.run(debug=True)
