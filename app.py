import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

from pymongo import MongoClient

client = MongoClient('mongodb://54.237.231.185', 27017, username="test", password="test")
db = client.dbsparta_plus_week4


# HTML을 주는 부분
# 접속시 jwt 토큰 확인 후 토큰 일치시 게임목록으로 보내고
# 미일치 시 로그인 창으로 보냄
@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"u_id": payload["id"]})
        user_id = user_info['u_id']
        user_nick = user_info['nick']
        return render_template('gamelist.html', user_info=user_info, user_nick=user_nick, user_id=user_id)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("in_home", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("in_home"))


@app.route('/home')
def in_home():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


# 로그인 기능
@app.route('/api/login', methods=['POST'])
def sign_in():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.user.find_one({'u_id': username_receive, 'u_pw': pw_hash})

    if result is not None:
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': "success", 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': "fail", 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


# 회원가입
@app.route('/api/membership', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    nickname_receive = request.form['nickname_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "u_id": username_receive,  # 아이디
        "u_pw": password_hash,  # 비밀번호
        "nick": nickname_receive,  # 프로필 이름 기본값은 아이디
    }
    db.user.insert_one(doc)
    return jsonify({'result': 'success'})


# 중복체크(아이디)
@app.route('/sign_up/check_id', methods=['POST'])
def check_id():
    username_receive = request.form['username_give']
    exists = bool(db.user.find_one({"u_id": username_receive}))
    print(exists)
    return jsonify({'result': 'success', 'exists': exists})

# 중복체크(닉네임)
@app.route('/sign_up/check_nick', methods=['POST'])
def check_nick():
    nickname_receive = request.form['nickname_give']
    exists = bool(db.user.find_one({"nick": nickname_receive}))
    print(exists)
    return jsonify({'result': 'success', 'exists': exists})

@app.route('/gamelist')
def gamelist():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"u_id": payload["id"]})
        user_nick = user_info['nick']
        return render_template('gamelist.html', result="success", user_nick=user_nick)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("in_home", msg="권한이 없습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("in_home", msg="권한이 없습니다."))


@app.route('/makegamelist')
def mkgame():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"u_id": payload["id"]})
        user_nick = user_info['nick']
        return render_template('makegamelist.html', result="success", user_nick=user_nick)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("in_home", msg="권한이 없습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("in_home", msg="권한이 없습니다."))


@app.route('/membership')
def membership():
    return render_template('membership.html')


@app.route('/posting/<keyword>')
def posting(keyword):
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        user_info = db.user.find_one({"u_id": payload["id"]})
        user_nick = user_info['nick']
        game_name = keyword
        return render_template('posting.html', user_info=user_info, user_nick=user_nick, game_name=game_name)
    except jwt.ExpiredSignatureError:
        return redirect(url_for("in_home", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("in_home", msg="로그인 정보가 존재하지 않습니다."))

@app.route("/room/gameimage", methods=["POST"])
def roomimage_get():
    gamename_receive = request.form['g_give']
    game_info = db.games.find_one({"G_name": gamename_receive})
    img_receive = game_info['Img']
    return jsonify({'img_src': img_receive})

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


# game 이름과 image를 POST
@app.route("/game", methods=["POST"])
def game_post():
    game_receive = request.form['game_give']

    file = request.files["file_give"]

    extension = file.filename.split('.')[-1]
    today = datetime.now()
    mytime = today.strftime('%Y-%m-%d-%H-%M-%S')
    filename = f'file-{mytime}'

    save_to = f'static/img/{filename}.{extension}'
    file.save(save_to)

    doc = {
        'G_name': game_receive,
        'Img': f'{filename}.{extension}'
    }
    db.games.insert_one(doc)

    return jsonify({'msg': '게임 목록 추가 완료!'})


# game 이름과 image를 GET
@app.route("/game", methods=["GET"])
def game_get():
    game_list = list(db.games.find({}, {'_id': False}))
    return jsonify({'games': game_list})

# 중복체크(게임명칭)
@app.route('/game/name', methods=['POST'])
def game_check():
    game_receive = request.form['game_give']
    exists = bool(db.games.find_one({"G_name": game_receive}))
    print(exists)
    return jsonify({'result': 'success', 'exists': exists})

# user info get[조원영]
@app.route('/gamelist/get_info')
def info_get():
    info_list = list(db.user.find({}, {'_id': False}))
    return jsonify({'info': info_list})
    # 위는 게임만 아래는 좋아요 포함[코딩중 ㅠ]
    # token_receive = request.cookies.get('mytoken')
    # try:
    #     posts = list(db.games.find({}))
    #     payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
    #     for post in posts:
    #         post["_id"] = str(post["_id"])
    #         post["count_heart"] = db.hearts.count_documents({"post_id": post["_id"], "type": "heart"})
    #         post["heart_by_me"] = bool(
    #             db.hearts.find_one({"post_id": post["_id"], "type": "heart", "username": payload['id']}))
    #     return jsonify({"result": "success", "posts": post})
    # except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
    #     return redirect(url_for("home"))



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
