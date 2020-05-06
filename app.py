from flask import Flask, render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def hello():
  return "Hello World"

@app.route('/top')
def top():
  return "ここがトップ"

# @app.route('/good')
# def good():
#   return "Good"

@app.route('/user/<name>')
def user(name):
  return "名前は"+name

@app.route('/name/<name>')
def name(name):
  return render_template("index.html",user_name = name)

@app.route('/temptest')
def temptest():
  name = "スナバコ"
  age = 27
  address = "香川県"
  return render_template("index.html", name = name, age = age, address = address)

@app.route('/weather')
def weather():
  takamatsu = 370000
  import requests
  url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
  payload = {'city':takamatsu}
  tenki_data = requests.get(url, params=payload).json()
  return render_template("weather.html", title = tenki_data['title'], date = tenki_data['forecasts'][0]['date'], tenki = tenki_data['forecasts'][0]['telop'], temperature_max = tenki_data['forecasts'][0]['temperature']['max']['celsius'], temperature_min = tenki_data['forecasts'][0]['temperature']['min']['celsius'])


# @app.route('/weather')
# def weather():
#   weather = "いい天気"
#   return render_template("weather.html", weather = weather)

@app.route('/dbtest')
def dbtest():
  # flasktest.dbに接続
  conn = sqlite3.connect("flasktest.db")
  # 中を見れるように
  c = conn.cursor()
  # sql文を実行
  c.execute("select name,age,address from users")
    # 変数にSQL文で取ってきた内容を格納
  user_info = c.fetchone()
  #DB接続終了 
  c.close()
  # 変数の中身を確認
  print(user_info)

  return render_template("dbtest.html", user_info = user_info)

@app.errorhandler(404)
def notfound(code):
  return "何もないよ！"

@app.route('/add', methods=["POST","GET"])
def add():
  return render_template("add.html")

if __name__ == "__main__":
  app.run(debug=True)