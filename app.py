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

##room post와 get
@app.route("/room", methods=["POST"])
def room_post():
    room_list = list(db.room.find({}, {'_id': False}))
    count = len(room_list) + 1
    gname_receive = request.form['gname_give']
    title_receive = request.form['title_give']
    desc_receive = request.form['desc_give']
    totalnum_receive = request.form['totalnum_give']
    date_receive = request.form['date_give']
    time_receive = request.form['time_give']
    nick_receive = request.form['nick_give']
    plist = []
    plist.append(nick_receive)

    doc = {
        'rid':count,
        'gname':gname_receive,
        'title':title_receive,
        'desc':desc_receive,
        'totalnum':totalnum_receive,
        'num':1,
        'date':date_receive,
        'time':time_receive,
        'nick':nick_receive,
        'participate':plist
    }
    db.room.insert_one(doc)

    return jsonify({'msg':'모집 게시글 작성 완료!'})

@app.route("/room", methods=["GET"])
def room_get():
    room_list = list(db.room.find({},{'_id':False}))
    return jsonify({'room':room_list})


if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)