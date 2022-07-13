
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
     └── /main.css
  └──/img
  └──/js
     ├── /gamelist.js
     └── /login.js
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
        <td width="12%">메인화면 페이지 로드</td>
        <td width="5%">GET</td>
        <td width="12%">/</td>
        <td width="30%"></td>
        <td width="31%">Token 검증됨 - render_template("layout_postlist.html", postdata=postdata)<br>Token 검증 안됨 - url_for("login", msg="로그인 정보가 존재하지 않습니다.")</td>
    </tr>
    <tr>
        <td width="12%">로그인 페이지 로드</td>
        <td width="5%">GET</td>
        <td width="12%">/login</td>
        <td width="30%">msg</td>
        <td width="31%">render_template('login.html', msg=msg)</td>
    </tr>
    <tr>
        <td width="12%">회원가입 페이지 로드</td>
        <td width="5%">GET</td>
        <td width="12%">/joinMembership</td>
        <td width="30%"></td>
        <td width="31%">render_template('join_membership.html')</td>
    </tr>
    <tr>
        <td width="12%">글쓰기 페이지 로드</td>
        <td width="5%">GET</td>
        <td width="12%">/writing</td>
        <td width="30%"></td>
        <td width="31%">Token 검증됨 - render_template('layout_writing.html')<br>Token 검증 안됨 - url_for("login", msg="로그인 정보가 존재하지 않습니다.")</td>
    </tr>
    <tr>
        <td width="12%">회원가입</td>
        <td width="5%">POST</td>
        <td width="12%">/signUp</td>
        <td width="30%">{'id': user_id,  'pw': user_password}</td>
        <td width="31%">{'msg': '회원가입이 완료되었습니다.'}</td>
    </tr>
    <tr>
        <td width="12%">ID 중복검사</td>
        <td width="5%">POST</td>
        <td width="12%">/check_dup</td>
        <td width="30%">{'id': check_id}</td>
        <td width="31%">중복 시 - {'msg': "사용 가능한 아이디 입니다."}<br>중복 아닐 시 - {'exists': "이미 존재하는 아이디 입니다."}</td>
    </tr>
    <tr>
        <td width="12%">로그인</td>
        <td width="5%">POST</td>
        <td width="12%">/api/login</td>
        <td width="30%">{'id': username_give, 'pw': password_give}</td>
        <td width="31%">로그인 성공 - {'result': 'success', 'token': token}<br>로그인 실패 - {'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'}</td>
    </tr>
    <tr>
        <td width="12%">글 저장</td>
        <td width="5%">POST</td>
        <td width="12%">/api/writing</td>
        <td width="30%">{'writer_name': writer_name, 'cafe_name': cafe_name, 'cafe_address': cafe_address, 'cafe_coment': cafe_coment, 'cafe_img': cafe_img, 'user_mentlist': user_mentlist}</td>
        <td width="31%">Token 검증됨 - {'msg': '저장되었습니다.'}<br>Token 검증 안됨 - url_for("login", msg="로그인 정보가 존재하지 않습니다.")</td>
    </tr>
    <tr>
        <td width="12%">상세 페이지 로드</td>
        <td width="5%">POST</td>
        <td width="12%">/<writer_name>/<cafe_name></td>
        <td width="30%">{'writer_name': writer_name, 'cafe_name': cafe_name}</td>
        <td width="31%">Token 검증됨 - render_template("layout_postview.html", writer_id=writer_id, cafe_name=cafe_name, cafe_address=cafe_address, cafe_img=cafe_img, cafe_coment=cafe_coment, user_mentlist=user_mentlist, current_user=user_id)<br>Token 검증 안됨 - url_for("login", msg="로그인 정보가 존재하지 않습니다.")</td>
    </tr>
    <tr>
        <td width="12%">댓글 저장</td>
        <td width="5%">POST</td>
        <td width="12%">/api/userment</td>
        <td width="30%">{'writer_name': writer_name, 'cafe_name': cafe_name, 'ment': user_ment_info}</td>
        <td width="31%">{'msg': '댓글이 저장되었습니다.'}</td>
    </tr>
    <tr>
        <td width="12%">댓글 삭제</td>
        <td width="5%">POST</td>
        <td width="12%">/api/delment</td>
        <td width="30%">{'writer_name': writer_name, 'cafe_name': cafe_name, 'ment': user_ment_info}</td>
        <td width="31%">{'msg': '댓글이 삭제되었습니다.'}</td>
    </tr>
    <tr>
        <td width="12%">현재 사용자 조회</td>
        <td width="5%">GET</td>
        <td width="12%">/api/getid</td>
        <td width="30%"></td>
        <td width="31%">Token 검증됨 - {'user_id': user_id}<br>Token 검증 안됨 - url_for("login", msg="로그인 정보가 존재하지 않습니다.")</td>
    </tr>
</table>

<br>

---

<h3 align="center"><b>멤버</b></h3>

---

<h3 align="center"><b>✏ Trouble Shooting ✏</b></h3>
<br>
