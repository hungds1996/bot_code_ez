from flask import *
from pymongo import *
from bot import Steam_guard_code

app = Flask(__name__)

app.config['SECRET_KEY'] = 'asdasd asas asqafkigk'


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

@app.route('/add_bot', methods = ['GET', 'POST'])
def add_bot():
    if request.method == 'GET':
        return render_template('new_bot.html')
    if request.method == 'POST':
        form = request.form
        bot_id = form['bot_id']
        bot_pass = form['bot_pass']
        code1 = form['code1']
        code2 = form['code2']
        code3 = form['code3']
        code4 = form['code4']
        code5 = form['code5']
        code6 = form['code6']

        new_bot = {
            'bot_id' : bot_id,
            'bot_pass' : bot_pass,
            'code' : [code1, code2, code3, code4, code5, code6]
        }
        bot_data.insert_one(new_bot)
        return redirect(url_for('bot'))

@app.route('/delete/<id>', methods = ['GET', 'POST'])
def delete(id):
    if request.method == 'GET':
        return render_template('confirm.html')
    if request.method == 'POST':
        bot_list = bot_data.find()
        picked_bot = bot_data.find_one({"bot_id": id})
        if picked_bot is None:
            return "not found"
        else:
            bot_data.delete_one({"bot_id": id})
            return redirect(url_for('bot'))

if __name__ == '__main__':
  app.run(debug=True)
