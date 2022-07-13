<h1 align="center">1주차 미니프로젝트 "Game_together"</h1>
<h4 align="center">2022.07.11 ~ 2022.07.14</h4>
<br>

---

<h3><b> 프로젝트 소개 </b></h3>
게임을 하고 싶지만 혼자 게임을 즐기기 외로울 때 같이 할 친구를 찾기 위해 만든 프로젝트입니다.
<br><br>

<h3><b> 프로젝트 시연영상 </b></h3>
""

---

<br>
<h3 align="center"><b>🛠 사용된 스택기술 🛠</b></h3>
<p align="center">


<br><br>
<h3 align="center"><b> 시작 설정 </b></h3>
<pre>
<code>
~$ cd sarangbang
~$ sudo chmod 755 initail_ec2.sh
~$ ./initial_ec2.sh
~$ pip install flask
~$ pip install mongo
~$ python3 app.py
</code>
</pre>

<br>
<h3 align="center"><b> 프로젝트 파일 구성 </b></h3>
<pre>
<code>
/static
  └──/css
     ├── /gamelist.css
     ├── /main.css
     └── /makegmaelist.css
  └──/img
  └──/js
     ├── /gamelist.js
     ├── /login.js
     └── /makegmaelist.js
/templates
  ├── /gamelist.html
  ├── /login.html
  ├── /makegamelist.html
  ├── /membership.html
  └── /posting.html

├── /README.md
├── /app.py
</code>
</pre>
<br>

---

<h3 align="center"><b> 메인 기능 설명</b></h3>

---

---

---

---

---

<br>
<h3 align="center"><b>🏷 API Table 🏷</b></h3>
<table width="100%">
    <tr align="center">
	<td width="12%"><b>기능</b></td>
        <td width="5%"><b>Method</b></td>
        <td width="12%"><b>URL</b></td>
        <td width="30%"><b>Request</b></td>
        <td width="31%"><b>Response</b></td>
    </tr>
    <tr>
        <td width="12%">게임 목록 페이지 로드</td>
        <td width="5%">GET</td>
        <td width="12%">/</td>
        <td width="30%"></td>
        <td width="31%">Token 검증 - render_template('gamelist.html', user_info=user_info, user_nick=user_nick)<br>Token 시간 만료시 - redirect(url_for("in_home", msg="로그인 시간이 만료되었습니다."))
Token 미검증 - redirect(url_for("in_home"))</td>
    </tr>
    <tr>
        <td width="12%">로그인 페이지 로드</td>
        <td width="5%">GET</td>
        <td width="12%">/home</td>
        <td width="30%">msg</td>
        <td width="31%">render_template('login.html', msg=msg)</td>
    </tr>
    <tr>
        <td width="12%">회원가입 페이지 로드</td>
        <td width="5%">GET</td>
        <td width="12%">/membership</td>
        <td width="30%"></td>
        <td width="31%">render_template('membership.html')</td>
    </tr>
    <tr>
        <td width="12%">게임 목록 추가 페이지 로드</td>
        <td width="5%">GET</td>
        <td width="12%">/makegamelist</td>
        <td width="30%"></td>
        <td width="31%">Token 검증 - render_template('gamelist.html', user_info=user_info, user_nick=user_nick)
Token 시간 만료시 - redirect(url_for("in_home", msg="로그인 시간이 만료되었습니다."))
Token 미검증 - redirect(url_for("in_home"))</td>
    </tr>
    <tr>
        <td width="12%">게임 채널 페이지 로드</td>
        <td width="5%">GET</td>
        <td width="12%">/posting/<keyword></td>
        <td width="30%"></td>
        <td width="31%">Token 검증 - render_template('gamelist.html', user_info=user_info, user_nick=user_nick)
Token 시간 만료시 - redirect(url_for("in_home", msg="권한이 없습니다."))
Token 미검증 - redirect(url_for("in_home, msg="권한이 없습니다."))</td>
    </tr>
    <tr>
        <td width="12%">로그인</td>
        <td width="5%">POST</td>
        <td width="12%">/api/login</td>
        <td width="30%">{'u_id': username_receive, 'u_pw': pw_hash}</td>
        <td width="31%">로그인 성공 - {'result': 'success', 'token': token}
로그인 실패 - {'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'}</td>
    </tr>
    <tr>
        <td width="12%">아이디 중복체크</td>
        <td width="5%">POST</td>
        <td width="12%">/sign_up/check_id</td>
        <td width="30%">{"u_id": username_receive}</td>
        <td width="31%">중복시 - {'msg':"이미 존재하는 아이디입니다."}
비 중복시 - {'msg':"사용할 수 있는 아이디입니다."}</td>
    </tr>
    <tr>
        <td width="12%">닉네임 중복체크</td>
        <td width="5%">POST</td>
        <td width="12%">/sign_up/check_nick</td>
        <td width="30%">{"nick": nickname_receive}</td>
        <td width="31%">중복시 - {'msg':"이미 존재하는 닉네임입니다."}
비 중복시 - {'msg':"사용할 수 있는 닉네임입니다."}</td>
    </tr>
    <tr>
        <td width="12%">회원가입</td>
        <td width="5%">POST</td>
        <td width="12%">/api/membership</td>
        <td width="30%">{"u_id": username_receive,"u_pw": password_hash, "nick": nickname_receive}</td>
        <td width="31%">{'msg': '회원가입이 완료되었습니다.'}</td>
    </tr>
    <tr>
        <td width="12%">게임채널 방등록</td>
        <td width="5%">POST</td>
        <td width="12%">/room</td>
        <td width="30%">{'rid': count,'gname': gname_receive,'title': title_receive,'desc': desc_receive,
'totalnum': int(totalnum_receive),'num': 1,'date': date_receive,
'time': time_receive,'nick': nick_receive,'participate': plist}</td>
        <td width="31%">빈칸 없을 시 - {'msg': '모집 게시글 작성 완료!'} 빈칸 있을 시 - {'msg': '빈칸을 다 채워주세요"}</td>
    </tr>
    <tr>
        <td width="12%">게임 채널 조회</td>
        <td width="5%">GET</td>
        <td width="12%">/room</td>
        <td width="30%">{'rid': count,'gname': gname_receive,'title': title_receive,'desc': desc_receive,
'totalnum': int(totalnum_receive),'num': 1,'date': date_receive,
'time': time_receive,'nick': nick_receive,'participate': plist}</td>
        <td width="31%">Token 검증 - render_template('gamelist.html', user_info=user_info, user_nick=user_nick)
Token 시간 만료시 - redirect(url_for("in_home", msg="권한이 없습니다."))
Token 미검증 - redirect(url_for("in_home, msg="권한이 없습니다."))</td>
    </tr>
    <tr>
        <td width="12%">게임 참가</td>
        <td width="5%">POST</td>
        <td width="12%">/room/in</td>
        <td width="30%">{'rid': int(rid_receive)}, {'$set': {'num': num}}
{'rid': int(rid_receive)}, {'$set': {'participate': party}}</td>
        <td width="31%">{'msg':'참가 완료!'}</td>
    </tr>
v
    <tr>
        <td width="12%">게임 퇴장</td>
        <td width="5%">POST</td>
        <td width="12%">/room/out</td>
        <td width="30%">{'rid': int(rid_receive)}, {'$set': {'num': num}}
{'rid': int(rid_receive)}, {'$set': {'participate': party}}</td>
        <td width="31%">{'msg':'취소완료!'}</td>
    </tr>
    <tr>
        <td width="12%">게임 참가 가능여부</td>
        <td width="5%">/room/check</td>
        <td width="12%">/sign_up/check_id</td>
        <td width="30%">{"u_id": username_receive}</td>
        <td width="31%">시간 지났을 경우 - {'msg':'마감완료!'}
자리가 있을 경우 - {'msg':'참가가 가능합니다}
인원이 가득찬경우 - {'msg':'자리가 가득 찼습니다'}[게임참가를 위한 변수로 사용]</td>
    </tr>
    <tr>
        <td width="12%">게임 참가 멤버 조회</td>
        <td width="5%">POST</td>
        <td width="12%">/room/showmember</td>
        <td width="30%">{'rid': int(rid_receive)}</td>
        <td width="31%">{'members': members}</td>
    </tr>
    <tr>
        <td width="12%">게임 제목 이미지 조회</td>
        <td width="5%">GET</td>
        <td width="12%">/game</td>
        <td width="30%"></td>
        <td width="31%">{'games': game_list}</td>
    </tr>
    <tr>
        <td width="12%">게임 제목 이미지 등록</td>
        <td width="5%">POST</td>
        <td width="12%">/game</td>
        <td width="30%">"{'G_name': game_receive,
        'Img': f'{filename}.{extension}'}"</td>
        <td width="31%">{'msg': '게임 목록 추가 완료!'}</td>
    </tr>
    <tr>
        <td width="12%">게임 제목 중복 체크</td>
        <td width="5%">GET</td>
        <td width="12%">/game/name</td>
        <td width="30%">{"G_name": game_receive}}</td>
        <td width="31%">{'msg':"게임명칭이 중복되었습니다.\n기존 게임방에 참여해주세요."}
{'msg':"추가할 수 있는 게임명칭입니다."}</td>
    </tr>
    <tr>
        <td width="12%">게임 목록에서 닉네임 표시</td>
        <td width="5%">GET</td>
        <td width="12%">/gamelist/get_info</td>
        <td width="30%"></td>
        <td width="31%">{'info': info_list}</td>
    </tr>


</table>

<br>

---

<h3 align="center"><b>멤버</b></h3>

---

<h3 align="center"><b>✏ Trouble Shooting ✏</b></h3>
<br>
