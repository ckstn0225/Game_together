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


function get_games() {
    $("#post-box").empty()
    $.ajax({
        type: "GET",
        url: `/get_posts?username_give=${username}`,
        data: {},
        success: function (response) {
            if (response["result"] == "success") {
                let posts = response["posts"]
                console.log(posts)
                for (let i = 0; i < posts.length; i++) {
                    let post = posts[i]
                    let time_post = new Date(post["date"])
                    let time_before = time2str(time_post)
                    let class_heart = post['heart_by_me'] ? "fa fa-heart" : "fa fa-heart-o"
                    let count_heart = post['count_heart']

                    function num2str(count) {
                        if (count > 10000) {
                            return parseInt(count / 1000) + "k"
                        }
                        if (count > 500) {
                            return parseInt(count / 100) / 10 + "k"
                        }
                        if (count == 0) {
                            return ""
                        }
                        return count
                    }

                    let html_temp = ``
                }
            }
        }
    })
}


function sign_out() {
    $.removeCookie('mytoken', {path: '/'});
    alert('로그아웃!')
    window.location.href = "/"
}