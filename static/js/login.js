
function login() {
    let username = $("#userid").val()
    let password = $("#userpw").val()

    if (username == "") {
        alert("아이디를 입력해주세요.")
        return;
    } else if (password == "") {
        alert("비밀번호를 입력해주세요.")
        return;
    } else {
        $.ajax({
            type: "POST",
            url: "/api/login",
            data: {
                username_give: username,
                password_give: password
            },
            success: function (response) {
                if (response['result'] == 'success') {
                    $.cookie('mytoken', response['token'], {path: '/'});
                    window.location.replace("/")
                } else {
                    alert(response['msg'])
                }
            }
        });
    }

}