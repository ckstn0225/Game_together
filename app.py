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
        'rid': count,
        'gname': gname_receive,
        'title': title_receive,
        'desc': desc_receive,
        'totalnum': int(totalnum_receive),
        'num': 1,
        'date': date_receive,
        'time': time_receive,
        'nick': nick_receive,
        'participate': plist
    }
    db.room.insert_one(doc)

    return jsonify({'msg': '모집 게시글 작성 완료!'})

@app.route("/room", methods=["GET"])
def room_get():
    room_list = list(db.room.find({}, {'_id': False}))
    return jsonify({'room': room_list})

##참가하기와 취소하기
@app.route("/room/in", methods=["POST"])
def room_in():
    rid_receive = request.form['rid_give']
    nick_receive = request.form['nick_give']
    room = db.room.find_one({'rid': int(rid_receive)})
    num = room['num'] + 1
    party = room['participate']
    party.append(nick_receive)
    db.room.update_one({'rid': int(rid_receive)}, {'$set': {'num': num}})
    db.room.update_one({'rid': int(rid_receive)}, {'$set': {'participate': party}})
    return jsonify({'msg': '참가 완료!'})

@app.route("/room/out", methods=["POST"])
def room_out():
    rid_receive = request.form['rid_give']
    nick_receive = request.form['nick_give']
    room = db.room.find_one({'rid': int(rid_receive)})
    num = room['num'] - 1
    party = room['participate']
    party.remove(nick_receive)
    db.room.update_one({'rid': int(rid_receive)}, {'$set': {'num': num}})
    db.room.update_one({'rid': int(rid_receive)}, {'$set': {'participate': party}})
    return jsonify({'msg': '취소 완료!'})

##충돌 방지 체크
@app.route("/room/check", methods=["POST"])
def room_check():
    rid_receive = request.form['rid_give']
    d = []
    d.append(request.form['y'])
    d.append(request.form['m'])
    d.append(request.form['d'])
    d.append(request.form['h'])
    d.append(request.form['mi'])

    room = db.room.find_one({'rid': int(rid_receive)})
    ddate = room['date']
    dtime = room['time']
    ddatel = ddate.split('-')
    dtimel = dtime.split(':')

    c = True

    if int(ddatel[0]) < int(d[0]):
        c = False
    elif int(ddatel[0]) > int(d[0]):
        c = True
    else:
        if int(ddatel[1]) < int(d[1]):
            c = False
        elif int(ddatel[1]) > int(d[1]):
            c = True
        else:
            if int(ddatel[2]) < int(d[2]):
                c = False
            elif int(ddatel[2]) > int(d[2]):
                c = True
            else:
                if int(dtimel[0]) < int(d[3]):
                    c = False
                elif int(dtimel[0]) > int(d[3]):
                    c = True
                else:
                    if int(dtimel[1]) < int(d[4]):
                        c = False
                    else:
                        c = True

    num = room['num']
    tnum = room['totalnum']
    msg = '시간이 지났습니다'

    if c:
        if num < tnum:
            msg = '참가가 가능합니다'
            c = True
        else:
            msg = '자리가 가득 찼습니다'
            c = False
    return jsonify({'msg': msg, 'check': c})

##멤버보기 기능
@app.route("/room/showmember", methods=["POST"])
def room_showmember():
    rid_receive = request.form['rid_give']
    room = db.room.find_one({'rid': int(rid_receive)})
    members = room['participate']
    return jsonify({'members': members})

#game 이름과 image를 POST
@app.route("/game", methods=["POST"])
def game_post():
    gname_receive = request.form['gname_give']
    # 이미지 추가 구현 필요 - hoisub
    image_receive = request.form['image_give']

    doc = {
        'gname': gname_receive,
        # 이미지 추가 구현 필요 - hoisub
        'image': image_receive
    }
    db.game.insert_one(doc)

    return jsonify({'msg': '게임 목록 추가 완료!'})

#game 이름과 image를 GET
@app.route("/game", methods=["GET"])
def game_get():
    game_list = list(db.game.find({},{'_id':False}))
    return jsonify({'game':game_list})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)