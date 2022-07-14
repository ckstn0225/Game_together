//게임 목록 불러오기
$(document).ready(function () {
    get_games()
})


function get_games() {
    $.ajax({
            type: "GET",
            url: `/game`,
            data: {},
            success: function (response) {
                let posts = response[0]['games']
                let rooms = response[1]['rooms']
                console.log(posts)
                console.log(rooms)
                for (let i = 0; i < posts.length; i++) {
                    let gamename = posts[i]['G_name']
                    let gameimg = posts[i]['Img']
                    let count = 0;
                    for(let i=0; i < rooms.length; i++) {
                        if (rooms[i]['gname'] == gamename) {
                            count++;
                        }
                    }
                    console.log(rooms[i])

                    console.log(gamename)
                    let html_temp = ``

                    if(gameimg.indexOf('file') == -1) {
                        html_temp = `<div class="card to_left g_box">                    
                                        <div class="card-image">
                                            <img src="${gameimg}"
                                                 class="g_image" alt="Placeholder image">
                                        </div>
                                        <div class="card-content G_name">
                                            ${gamename}
                                        </div>
                                        <button class="button is-info b_jump" onclick='to_room("${gamename}")'>채널접속</button>
                                    <div>현재 게임방 ${count}개</div>
                                    </div>`
                    } else {
                        html_temp = `<div class="card to_left g_box">
                                        <div class="card-image">
                                            <img src="../static/img/${gameimg}"
                                                 class="g_image" alt="Placeholder image">
                                        </div>
                                        <div class="card-content G_name">
                                            ${gamename}
                                        </div>
                                        <button class="button is-info b_jump" onclick='to_room("${gamename}")'>채널접속</button>
                                    <div>현재 게임방 ${count}개</div>
                                    </div>`
                    }
                    $("#games").append(html_temp)

                }
                let footer_html = `<nav class="tabs is-boxed is-fullwidth" style="margin-bottom: 40px">
                                    <div class="container">
                                        <ul style="float:right;">
                                            <button onclick="makegamelist()" class="button" style="font-family: 'Gamja Flower', cursive;">게임목록추가
                                            </button>
                                        </ul>
                                    </div>
                                </nav>`
                $('#wrap').append(footer_html)
            }
        }
    )
}

//방으로 이동 시 방번호 지정
function to_room(game,img) {
               window.location.href = `/posting/${game}`
            }


//로그아웃 및 쿠키삭제
function sign_out() {
    $.removeCookie('mytoken', {path: '/'});
    alert('로그아웃!')
    window.location.href = "/"
}

function makegamelist() {
   window.location.href = "/makegamelist"
}