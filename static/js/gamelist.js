function toggle_like(gamename, type) {
    console.log(gamename, type)
    let $a_like = $(`#${post_id} a[aria-label='heart']`)
    let $i_like = $a_like.find("i")
    if ($i_like.hasClass("fa-heart")) {
        $.ajax({
            type: "POST",
            url: "/update_like",
            data: {
                post_id_give: post_id,
                type_give: type,
                action_give: "unlike"
            },
            success: function (response) {
                console.log("unlike")
                $i_like.addClass("fa-heart-o").removeClass("fa-heart")
                $a_like.find("span.like-num").text(response["count"])
            }
        })
    } else {
        $.ajax({
            type: "POST",
            url: "/update_like",
            data: {
                post_id_give: post_id,
                type_give: type,
                action_give: "like"
            },
            success: function (response) {
                console.log("like")
                $i_like.addClass("fa-heart").removeClass("fa-heart-o")
                $a_like.find("span.like-num").text(response["count"])
            }
        })

    }
}

//게임 목록 불러오기
$(document).ready(function () {
    get_games()
})


function get_games() {
    $.ajax({
            type: "GET",
            url: `/get_list`,
            data: {},
            success: function (response) {
                let posts = response['games']
                console.log(posts)
                for (let i = 0; i < posts.length; i++) {
                    let gamename = posts[i]['G_name']
                    let gameimg = posts[i]['Img']
                    let gameid = posts[i]['id']
                    let html_temp = `<div class="card to_left" onclick='to_room("${gameid}")'>
                                        <div class="card-image">
                                            <img src="${gameimg}"
                                                 alt="Placeholder image">
                                        </div>
                                        <div class="card-content G_name">
                                            ${gamename}
                                        </div>
                                    </div>`
                    $("#games").append(html_temp)

                }
            }
        }
    )
}

//방으로 이동 시 방번호 지정
function to_room(game) {
        $.ajax({
            type: "POST",
            url: "/channel",
            data: {
                gamename_give: game
            },
            success: function (response) {
                console.log(game)
            }
        });
}

//로그아웃 및 쿠키삭제
function sign_out() {
    $.removeCookie('mytoken', {path: '/'});
    alert('로그아웃!')
    window.location.href = "/"
}