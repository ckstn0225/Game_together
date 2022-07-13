let isGameChecked = false;
let result = false;

$(document).ready(function () {
    bsCustomFileInput.init()
})

function image_add(input) {
    let file = input.files[0];
    let newImage = document.createElement("img");
    newImage.setAttribute("class", "img");

    newImage.src = URL.createObjectURL(file);

    newImage.style.width = "auto";
    newImage.style.height = "140px";
    newImage.style.objectFit = "contain";

    let container = document.getElementById('show-image');
    $('#show-image').empty()
    container.appendChild(newImage);
}

function game_check() {
    let game = $('#game').val()
    if (game == "") {
        $('#help-game').text("게임명칭을 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        return;
    }

    $.ajax({
        type: "POST",
        url: "/game/name",
        data: {
            game_give: game
        },
        success: function (response) {
            result = response["exists"]
            if (result) {
                alert("게임명칭이 중복되었습니다.\n기존 게임방에 참여해주세요.")
                $('#help-game').text("게임명칭을 재입력해주세요.").removeClass("is-safe").addClass("is-danger")
            } else {
                $('#help-game').text("추가할 수 있는 게임명칭입니다.").removeClass("is-danger").addClass("is-safe")
            }
            isGameChecked = true
        }
    });
}

function game_add() {
    let game = $('#game').val()

    let file = $('#file')[0].files[0]

    if (game == "") {
        alert("게임명칭을 입력해주세요.")
        $('#help-game').text("게임명칭을 입력해주세요.").removeClass("is-safe").addClass("is-danger")
        return;
    } else if (file == null) {
        alert("이미지를 추가해주세요.")
        $('#help-image').text("이미지를 추가해주세요.").removeClass("is-safe").addClass("is-danger")
        return;
    } else if (isGameChecked == false) {
        alert("게임명칭 중복체크를 해주세요.")
        $('#help-game').text("게임명칭 중복체크를 해주세요.").removeClass("is-safe").addClass("is-danger")
        return;
    } else if (result == true) {
        alert("게임명칭이 중복되었습니다.\n기존 게임방에 참여해주세요.")
        $('#help-game').text("게임명칭을 재입력해주세요.").removeClass("is-safe").addClass("is-danger")
        return;
    }
    let form_data = new FormData()

    form_data.append("file_give", file)
    form_data.append("game_give", game)

    $.ajax({
        type: "POST",
        url: "/game",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["msg"])
            window.location.href = `/gamelist`
        }
    });
}

function get_game_test() {
    $('#card-box').removeAttr('hidden', 'true')
    $.ajax({
        type: "GET",
        url: "/game",
        data: {},
        success: function (response) {
            let games = response['games']
            for (let i = 0; i < games.length; i++) {
                let G_name = games[i]['G_name']
                let Img = games[i]['Img']
                console.log(G_name, Img)
                let temp_html = `<div class="col">
                                            <div class="card">
                                                <img src="../static/img/${Img}" class="card-img-top" alt="...">
                                                <div class="card-body">
                                                    <h5 class="card-title">${G_name}</h5>
                                                    <p class="card-text">${G_name}</p>
                                                </div>
                                            </div>
                                          </div>`
                $('#card-box').append(temp_html)
            }
        }
    });
}

//로그아웃 및 쿠키삭제
function sign_out() {
    $.removeCookie('mytoken', {path: '/'});
    alert('로그아웃!')
    window.location.href = "/"
}