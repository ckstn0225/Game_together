from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://test:sparta@sparta.mtxvxou.mongodb.net/sparta?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


## HTML을 주는 부분
# 들어오면 로그인 화면으로
@app.route('/')
def home():
   return render_template('login.html')

@app.route('/gamelist')
def gamelist():
   return render_template('gamelist.html')

@app.route('/makegamelist')
def mkgame():
   return render_template('makegamelist.html')

@app.route('/membership')
def membership():
   return render_template('membership.html')

@app.route('/posting')
def posting():
   return render_template('posting.html')

@app.route('/memo', methods=['GET'])
def listing():
    return jsonify({'all_articles':articles})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    return jsonify({'msg':'저장이 완료되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)