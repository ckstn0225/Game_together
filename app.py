from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi
ca = certifi.where()
client = MongoClient('mongodb+srv://Test:sparta@cluster0.iwfou.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta


## HTML을 주는 부분
# 들어오면 로그인 화면으로
@app.route('/')
def home():
   return render_template('login.html')

@app.route('/memo', methods=['GET'])
def listing():
    return jsonify({'all_articles':articles})

## API 역할을 하는 부분
@app.route('/memo', methods=['POST'])
def saving():
    return jsonify({'msg':'저장이 완료되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)