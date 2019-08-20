function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function updatepwd() {
    if ($("#confirmPassword").val() != $("#password").val()) {
        alert('密码不一致');
        $("#confirmPassword").css("border", "1px solid red");
        return false;
    }
    if ($("#old_password").val() == "") {
        alert('旧密码不能为空');
        return false;
    }
    if ($("#password").val() == "") {
        alert('新密码不能为空');
        return false;
    }
    $.ajax({
        cache: false,
        type: "POST",
        dataType: 'json',
        url: "/users/update/pwd/",
        data: $('#reset-pwd-form').serialize(),
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            if (data.msg == '旧密码错误') {

                $("#old_password").css("border", "1px solid red");
                $("#old_password").val('');
                $("#old_password").attr("placeholder", '旧密码错误');
            }
            else if (data.msg == '密码修改成功') {
                $('#modal_change_pwd').modal('hide');
                window.location.reload()

            }
            else {
                alert(data.msg);
            }
        }
    });
}


function submit_unbind_email() {
    if ($("#email").val() == "") {
        alert('邮箱不能为空');
        $("#email").css("border", "1px solid red");
        return false;
    }
    if ($("#verify_code").val() == "") {
        alert('图形验证码不能为空');
        $("#verify_code").css("border", "1px solid red");
        return false;
    }


    $.ajax({
        cache: false,
        type: "POST",
        dataType: 'json',
        url: "/users/unbind/email/",
        data: $('#unbind-email-form').serialize(),
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            refresh_code($("#code"));
            if (data.status == "fail") {
                if (data.msg.indexOf('邮箱') > -1) {
                    layer.tips(data.msg, $("#email"));
                }
                else if (data.msg == "图形验证码错误") {
                    layer.tips(data.msg, $("#verify_code"));
                } else {
                    layer.tips(data.msg, $("#submit_unbind_email"));
                }
                return false;

            }
            else {
                layer.closeAll();
                window.location.reload();
            }

        }
    });

}

function submit_unbind_mobile() {
    if ($("#mobile").val() == "") {
        alert('手机号不能为空');
        $("#mobile").css("border", "1px solid red");
        return false;
    }
    if ($("#verify_code").val() == "") {
        alert('图形验证码不能为空');
        $("#verify_code").css("border", "1px solid red");
        return false;
    }


    $.ajax({
        cache: false,
        type: "POST",
        dataType: 'json',
        url: "/users/unbind/mobile/",
        data: $('#unbind-mobile-form').serialize(),
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            refresh_code($("#code"));
            if (data.status == "fail") {
                if (data.msg.indexOf('手机') > -1) {
                    layer.tips(data.msg, $("#mobile"));
                }
                else if (data.msg == "图形验证码错误") {
                    layer.tips(data.msg, $("#verify_code"));
                } else {
                    layer.tips(data.msg, $("#submit_unbind_mobile"));
                }
                return false;

            }
            else {
                layer.closeAll();
                window.location.reload();
            }

        }
    });

}


function submit_bind_email() {
    if ($("#emai").val() == "") {
        alert('邮箱不能为空');
        $("#emai").css("border", "1px solid red");
        return false;
    }
    if ($("#verify_code").val() == "") {
        alert('图形验证码不能为空');
        $("#verify_code").css("border", "1px solid red");
        return false;
    }
    if ($("#email_code").val() == "") {
        alert('邮箱验证码不能为空');
        $("#email_code").css("border", "1px solid red");
        return false;
    }

    $.ajax({
        cache: false,
        type: "POST",
        dataType: 'json',
        url: "/users/update/email/",
        data: $('#bind-email-form').serialize(),
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            refresh_code($("#code"));
            if (data.status == "fail") {
                alert(data.msg);
                return false;

            }
            else {
                layer.closeAll();
                window.location.reload();
            }

        }
    });

}

function submit_bind_mobile() {
    if ($("#mobile").val() == "") {
        alert('手机号不能为空');
        $("#mobile").css("border", "1px solid red");
        return false;
    }
    if ($("#verify_code").val() == "") {
        alert('图形验证码不能为空');
        $("#verify_code").css("border", "1px solid red");
        return false;
    }
    if ($("#sms_code").val() == "") {
        alert('短信验证码不能为空');
        $("#sms_code").css("border", "1px solid red");
        return false;
    }

    $.ajax({
        cache: false,
        type: "POST",
        dataType: 'json',
        url: "/users/update/mobile/",
        data: $('#bind-mobile-form').serialize(),
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            refresh_code($("#code"));
            if (data.status == "fail") {
                alert(data.msg);
                return false;

            }
            else {
                layer.closeAll();
                window.location.reload();
            }

        }
    });

}

function change_auth(tt) {

    layer.open({
        type: 1,
        title: false,
        area: ['490px', '300px'],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'sbs_form_css',
        content: '            <div id="page-change-pwd" style="position:relative;display: block;">\n' +
        '\n' +
        '                <div class="comment_section" style="width: 490px;padding: 22px 22px;min-height: 280px">\n' +
        '                    <div style="position: relative;">\n' +
        '                        <p class="head-title">验证密码</p>\n' +
        '                    </div>\n' +
        '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
        '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n' +
        '                    <form id="reset-pwd-form" style="text-align: center;margin-top: 60px">\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">当前密码:</span>\n' +
        '                            <input id="password" type="password" name="password"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +
        '                        <div onclick="checkpwd()" style="margin-top: 24px" class="small_btn">提交</div>\n' +
        '                    </form>\n' +
        '                </div>\n' +
        '\n' +
        '            </div>'
    });

    oper = tt;
}

//验证密码
function checkpwd() {

    if ($("#password").val() == "") {
        alert("密码不能为空");
        return false;
    }
    $.ajax({
        cache: false,
        type: "POST",
        dataType: 'json',
        url: "/users/checkpwd/",
        data: {password: $("#password").val()},
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            if (data.status == 0) {
                //打开下一个moddal,隐藏当前modal
                layer.closeAll();
                if (oper == 'changepwd') {
                    $('#modal_change_pwd').modal('show');
                } else if (oper == "bindmobile") {

                    layer.open({
                        type: 1,
                        title: false,
                        area: ['490px', '300px'],
                        closeBtn: 0,
                        shadeClose: false,
                        scrollbar: false,
                        skin: 'sbs_form_css',
                        content: '            <div id="page-change-pwd" style="position:relative;display: block;">\n' +
                        '\n' +
                        '                <div class="comment_section" style="width: 490px;padding: 22px 22px;min-height: 280px">\n' +
                        '                    <div style="position: relative;">\n' +
                        '                        <p class="head-title">绑定手机号</p>\n' +
                        '                    </div>\n' +
                        '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
                        '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n' +
                        '                    <form id="bind-mobile-form" style="text-align: center">\n' +
                        '                        <div style="margin-top: 20px">\n' +
                        '                            <span class="label_sbs">手机号:</span>\n' +
                        '                            <input id="mobile" type="tel" name="mobile"\n' +
                        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
                        '                        </div>\n' +
                        '                        <div style="margin-top: 20px">\n' +
                        '                            <span class="label_sbs">验证码:</span>\n' +
                        '                            <input id="verify_code" type="text" maxlength="4" name="verify_code"\n' +
                        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px"> <img style="width: 100px;\n' +
                        '    height: 35px;" onclick="refresh_code(this)" src="/users/verify_code/">\n' +
                        '                        </div>\n' +
                        '                        <div style="margin-top: 20px;    padding-right: 27px;">\n' +
                        '                            <span class="label_sbs">手机验证码:</span>\n' +
                        '                            <input id="sms_code" type="text" maxlength="4" name="sms_code"\n' +
                        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px">' +
                        '<div id="get_sms_code" onclick="get_sms_code(this,\'bind_mobile\')" class="smscode">获取验证码</div>\n' +
                        '                        </div>\n' +
                        '                        <div onclick="submit_bind_mobile()" style="margin-top: 24px" class="small_btn">提交</div>\n' +
                        '                    </form>\n' +
                        '                </div>\n' +
                        '\n' +
                        '            </div>'
                    });

                } else if (oper == "unbindmobile") {

                    layer.open({
                        type: 1,
                        title: false,
                        area: ['490px', '300px'],
                        closeBtn: 0,
                        shadeClose: false,
                        scrollbar: false,
                        skin: 'sbs_form_css',
                        content: '            <div id="page-change-pwd" style="position:relative;display: block;">\n' +
                        '\n' +
                        '                <div class="comment_section" style="width: 490px;padding: 22px 22px;min-height: 280px">\n' +
                        '                    <div style="position: relative;">\n' +
                        '                        <p class="head-title">解绑手机号</p>\n' +
                        '                    </div>\n' +
                        '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
                        '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n' +
                        '                    <form id="unbind-mobile-form" style="text-align: center">\n' +
                        '                        <div style="margin-top: 20px">\n' +
                        '                            <span class="label_sbs">手机号:</span>\n' +
                        '                            <input id="mobile" type="tel" name="mobile"\n' +
                        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
                        '                        </div>\n' +
                        '                        <div style="margin-top: 20px">\n' +
                        '                            <span class="label_sbs">验证码:</span>\n' +
                        '                            <input id="verify_code" type="text" maxlength="4" name="verify_code"\n' +
                        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px"> <img style="width: 100px;\n' +
                        '    height: 35px;" onclick="refresh_code(this)" src="/users/verify_code/">\n' +
                        '                        </div>\n' +
                        '                        <div id="submit_unbind_mobile" onclick="submit_unbind_mobile()" style="margin-top: 24px" class="small_btn">提交</div>\n' +
                        '                    </form>\n' +
                        '                </div>\n' +
                        '\n' +
                        '            </div>'
                    });


                } else if (oper == "bindemail") {

                    layer.open({
                        type: 1,
                        title: false,
                        area: ['490px', '300px'],
                        closeBtn: 0,
                        shadeClose: false,
                        scrollbar: false,
                        skin: 'sbs_form_css',
                        content: '            <div id="page-change-pwd" style="position:relative;display: block;">\n' +
                        '\n' +
                        '                <div class="comment_section" style="width: 490px;padding: 22px 22px;min-height: 280px">\n' +
                        '                    <div style="position: relative;">\n' +
                        '                        <p class="head-title">绑定邮箱</p>\n' +
                        '                    </div>\n' +
                        '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
                        '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n' +
                        '                    <form id="bind-email-form" style="text-align: center">\n' +
                        '                        <div style="margin-top: 20px">\n' +
                        '                            <span class="label_sbs">邮箱:</span>\n' +
                        '                            <input id="email" type="email" name="email"\n' +
                        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
                        '                        </div>\n' +
                        '                        <div style="padding-right:11px;margin-top: 20px">\n' +
                        '                            <span class="label_sbs">验证码:</span>\n' +
                        '                            <input id="verify_code" type="text" maxlength="4" name="verify_code"\n' +
                        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px"> <img style="width: 100px;\n' +
                        '    height: 35px;" onclick="refresh_code(this)" src="/users/verify_code/">\n' +
                        '                        </div>\n' +
                        '                        <div style="margin-top: 20px;    padding-right: 38px;">\n' +
                        '                            <span class="label_sbs">邮箱验证码:</span>\n' +
                        '                            <input id="email_code" type="text" maxlength="4" name="email_code"\n' +
                        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px">' +
                        '<div id="get_email_code" onclick="get_email_code(this,\'bind_email\')" class="smscode">获取验证码</div>\n' +
                        '                        </div>\n' +
                        '                        <div onclick="submit_bind_email()" style="margin-top: 24px" class="small_btn">提交</div>\n' +
                        '                    </form>\n' +
                        '                </div>\n' +
                        '\n' +
                        '            </div>'
                    });

                }
                else if (oper == "unbindemail") {
                    //
                    // $.ajax({
                    //     cache: false,
                    //     type: "POST",
                    //     dataType: 'json',
                    //     url: "/users/unbind/email/",
                    //     async: true,
                    //     beforeSend: function (xhr, settings) {
                    //         xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    //     },
                    //     success: function (data) {
                    //         alert(data.msg);
                    //         window.location.reload();
                    //     }
                    // });

                    layer.open({
                        type: 1,
                        title: false,
                        area: ['490px', '300px'],
                        closeBtn: 0,
                        shadeClose: false,
                        scrollbar: false,
                        skin: 'sbs_form_css',
                        content: '            <div id="page-change-pwd" style="position:relative;display: block;">\n' +
                        '\n' +
                        '                <div class="comment_section" style="width: 490px;padding: 22px 22px;min-height: 280px">\n' +
                        '                    <div style="position: relative;">\n' +
                        '                        <p class="head-title">解绑邮箱</p>\n' +
                        '                    </div>\n' +
                        '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
                        '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n' +
                        '                    <form id="unbind-email-form" style="text-align: center">\n' +
                        '                        <div style="margin-top: 20px">\n' +
                        '                            <span class="label_sbs">邮箱:</span>\n' +
                        '                            <input id="email" type="tel" name="email"\n' +
                        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
                        '                        </div>\n' +
                        '                        <div style="margin-top: 20px">\n' +
                        '                            <span class="label_sbs">验证码:</span>\n' +
                        '                            <input id="verify_code" type="text" maxlength="4" name="verify_code"\n' +
                        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px"> <img style="width: 100px;\n' +
                        '    height: 35px;" onclick="refresh_code(this)" src="/users/verify_code/">\n' +
                        '                        </div>\n' +
                        '                        <div id="submit_unbind_email" onclick="submit_unbind_email()" style="margin-top: 24px" class="small_btn">提交</div>\n' +
                        '                    </form>\n' +
                        '                </div>\n' +
                        '\n' +
                        '            </div>'
                    });


                }

            }
            else {
                alert('密码错误');
                $("#password").css("border", "1px solid red");
            }
        }
    });

}

function refresh_code(btn) {
    var timestamp = new Date().getTime();
    $(btn).attr('src', "/users/verify_code/?t=" + timestamp);
}


function get_email_code(thisBtn, type) {

    var doLoop = function () {
        nums--;
        if (nums > 0) {
            $(btn).html(nums + '秒');
        } else {
            clearInterval(clock); //清除js定时器
            btn.disabled = false;
            $(btn).html('获取验证码');
            $(btn).attr('onclick', "get_email_code(this,\'" + type + "\')");
            nums = 10; //重置时间
        }
    }


    var email = $("#email").val();
    if (email == "") {
        $("#email").attr("placeholder", '请输入邮箱');
        $("#email").focus();
        return false;
    }
    if ($("#verify_code").val() == "") {
        $("#verify_code").attr("placeholder", '请输入验证码');
        $("#verify_code").focus();
        return false;
    }

    clock = '';
    nums = 10;
    var csrftoken = getCookie('csrftoken');

    btn = thisBtn;
    $(btn).disabled = true; //将按钮置为不可点击
    $(btn).html(nums + '秒');
    $(btn).removeAttr('onclick');
    clock = setInterval(doLoop, 1000); //一秒执行一次

    $.ajax({
        cache: false,
        type: 'post',
        dataType: 'json',
        url: "/users/get_email_code/",
        data: {email: $("#email").val(), send_type: type, verify_code: $("#verify_code").val()},
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (data) {
            if (data.status == "success") {
                layer.tips('验证码已发送', $("#get_email_code"));
            }
            else {
                layer.tips(data.msg, $("#get_email_code"));
            }

        },
        error: function (xhr, textStatus) {
            console.log(xhr);
            console.log(textStatus);

        }
    });
}


function get_sms_code(thisBtn, type) {
    function countdown() {
        clock = setInterval(doLoop, 1000); //一秒执行一次
        btn = thisBtn;
        $(btn).disabled = true; //将按钮置为不可点击
        $(btn).html(nums + '秒');
        $(btn).removeAttr('onclick');
    }

    var doLoop = function () {
        nums--;
        if (nums > 0) {
            $(btn).html(nums + '秒');
        } else {
            clearInterval(clock); //清除js定时器
            btn.disabled = false;
            $(btn).html('获取验证码');
            $(btn).attr('onclick', "get_sms_code(this,\'" + type + "\')");
            nums = 60; //重置时间
        }
    }

    var mobile = $("#mobile").val();
    if (mobile == "" || mobile.length != 11) {
        $("#mobile").attr("placeholder", '请输入手机号');
        $("#mobile").focus();
        return false;
    }
    if ($("#verify_code").val() == "") {
        $("#verify_code").attr("placeholder", '请输入验证码');
        $("#verify_code").focus();
        return false;
    }
    clock = '';
    nums = 60;
    var csrftoken = getCookie('csrftoken');

    var url = "/users/get_sms_code/";
    if (type == "register" || type == "forget") {
        url = "/sms_code/";
    }
    $.ajax({
        cache: false,
        type: 'post',
        dataType: 'json',
        url: url,
        data: {mobile: $("#mobile").val(), send_type: type, verify_code: $("#verify_code").val()},
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        },
        success: function (data) {
            if (data.status == "success") {
                layer.tips('验证码已发送', $("#get_sms_code"));
                countdown();
            }
            else {
                layer.tips(data.msg, $("#get_sms_code"));
                if (data.msg == "验证码错误") {
                    refresh_code($("#code"));
                } else {
                    countdown();
                }

            }

        },
        error: function (xhr, textStatus) {
            console.log(xhr);
            console.log(textStatus);

        }
    });
}


//修改密码

$("#change_pwd").click(function () {
    layer.open({
        type: 1,
        title: false,
        area: ['490px', '300px'],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'sbs_form_css',
        content: '            <div id="page-change-pwd" style="position:relative;display: block;">\n' +
        '\n' +
        '                <div class="comment_section" style="width: 490px;padding: 22px 22px;min-height: 280px">\n' +
        '                    <div style="position: relative;">\n' +
        '                        <p class="head-title">修改密码</p>\n' +
        '                    </div>\n' +
        '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
        '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n' +
        '                    <form id="reset-pwd-form" style="text-align: center">\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">旧密码:</span>\n' +
        '                            <input id="old_password" type="password" name="old_password"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">新密码:</span>\n' +
        '                            <input id="password" type="password" name="password"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px;    padding-right: 27px;">\n' +
        '                            <span class="label_sbs">确认新密码:</span>\n' +
        '                            <input id="confirmPassword" type="password" name="confirmPassword"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +
        '                        <div onclick="updatepwd()" style="margin-top: 24px" class="small_btn">提交</div>\n' +
        '                    </form>\n' +
        '                </div>\n' +
        '\n' +
        '            </div>'
    });
    $("#confirmPassword").focusout(function () {

        if ($("#confirmPassword").val() != $("#password").val()) {

            $("#confirmPassword").css("border", "1px solid red");
        }
        else {
            $("#confirmPassword").css("border", "1px solid #fecc2e");
        }

    });
});

function updateReminder(btn, type, value) {

    $.ajax({
        cache: false,
        type: 'post',
        dataType: 'json',
        url: "/users/update/remind/",
        data: {type: type, value: value},
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            if (data.status == "success") {
                layer.tips(data.msg, $(btn));
            }
            else {
                layer.tips(data.msg, $(btn));
            }

        },
        error: function (xhr, textStatus) {
            console.log(xhr);
            console.log(textStatus);

        }
    });
}


function popforget_mobile() {
    layer.closeAll();
    layer.open({
        type: 1,
        title: false,
        area: ['500px', '400'],
        offset: ["28%", "20%"],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'myclas',
        content: '' +
        '\n' +
        '                <div class="comment_section" style="padding: 22px 22px;min-height: 250px">\n' +
        '                    <div style="position: relative;text-align: center;">\n' +
        '                        <p class="head-title"><span onclick="popforget_mobile()" class="mytab active">手机找回</span><span onclick="popforget_email()" class="mytab" style="margin-left: 20px">邮箱找回</span></p>\n' +
        '                    </div>\n' +
        '                    <form id="forget-form" style="text-align: center">\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">手机号:</span>\n' +
        '                            <input id="mobile" type="tel" name="mobile" placeholder="请输入手机号"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        <input type="hidden" name="forget_type" value="2"></div>\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">验证码:</span>\n' +
        '                            <input id="verify_code" type="text" maxlength="4" name="verify_code" autocomplete="off" placeholder="请输入验证码"\n' +
        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px"> <img id="code" style="width: 100px;\n' +
        '    height: 35px;" onclick="refresh_code(this)" src="/users/verify_code/">\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px;    padding-right: 27px;">\n' +
        '                            <span class="label_sbs">短信验证码:</span>\n' +
        '                            <input id="sms_code" type="text" maxlength="4" name="sms_code"\n' +
        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px">' +
        '<div id="get_sms_code" onclick="get_sms_code(this,\'forget\')" class="smscode">获取验证码</div>\n' +
        '                        </div>\n' +
        '                        <div id="forgetmobile" onclick="forget(2)" style="margin-top: 24px" class="small_btn">提交</div>\n' +
        '                    </form>\n' +
        '  <div class="label_sbs" style="margin-top:20px;text-align: center;padding-left: 55px;"><span>已有账号?</span><span class="btnoff"><a style="color: red" href="/login">立即登录</a></span></div>                                      ' +
        '                </div>\n'
    });
    $("#verify_code").html("");
    refresh_code($("#code"));

}

function popforget_email() {
    layer.closeAll();
    layer.open({
        type: 1,
        title: false,
        area: ['500px', '400'],
        offset: ["28%", "20%"],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'myclas',
        content: '' +
        '\n' +
        '                <div class="comment_section" style="padding: 22px 22px;min-height: 250px">\n' +
        '                    <div style="position: relative;text-align: center;">\n' +
        '                        <p class="head-title"><span onclick="popforget_mobile()" class="mytab ">手机找回</span><span onclick="popforget_email()" class="mytab active" style="margin-left: 20px">邮箱找回</span></p>\n' +
        '                    </div>\n' +
        '                    <form id="forget-form" style="text-align: center">\n' +
        '                        <div style="margin-top: 20px;padding-left: 13px;">\n' +
        '                            <span class="label_sbs">邮箱:</span>\n' +
        '                            <input id="mobile" type="tel" name="mobile" placeholder="请输入邮箱"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        <input type="hidden" name="forget_type" value="1"></div>\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">验证码:</span>\n' +
        '                            <input id="verify_code" type="text" maxlength="4" name="verify_code" autocomplete="off" placeholder="请输入验证码"\n' +
        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px"> <img id="code" style="width: 100px;\n' +
        '    height: 35px;" onclick="refresh_code(this)" src="/users/verify_code/">\n' +
        '                        </div>\n' +
        '                        <div id="forgetemail" onclick="forget(1)" style="margin-top: 24px" class="small_btn">提交</div>\n' +
        '                    </form>\n' +
        '  <div class="label_sbs" style="margin-top:20px;text-align: center;padding-left: 55px;"><span>已有账号?</span><span class="btnoff"><a style="color: red" href="/login">立即登录</a></span></div>                                      ' +
        '                </div>\n'
    });
    $("#verify_code").html("");
    refresh_code($("#code"));

}

function forget(index) {

    if ($("#mobile").val() == "") {
        if (index == 1) {
            layer.tips('邮箱不能为空', $("#mobile"));
        }
        else {
            layer.tips('手机号不能为空', $("#mobile"));
        }
        $("#mobile").css("border", "1px solid red");
        return false;
    }
    if ($("#verify_code").val() == "") {
        layer.tips('图形验证码不能为空', $("#verify_code"));
        $("#verify_code").css("border", "1px solid red");
        return false;
    }

    $.ajax({
        cache: false,
        type: "POST",
        dataType: 'json',
        url: "/forget/",
        data: $('#forget-form').serialize(),
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            if (data.status == "fail") {
                if (index == 2) {
                    layer.tips(data.msg, $("#forgetmobile"));
                }
                else {
                    layer.tips(data.msg, $("#forgetemail"));
                }
                refresh_code("#code");
                return false;
            }
            else {
                if (index == 2) {
                    // layer.tips('手机验证码已发送', $("#forgetmobile"));
                    window.location.href = '/mobilereset/' + data.mobilecode;
                }
                else {
                    layer.tips('邮件发送成功，请查收！', $("#forgetemail"));
                    //for(var t = Date.now();Date.now() - t <= 5000;);
                    //window.location.href = '/login/';
                }
                // layer.closeAll();
                // layer.open({
                //     type: 1,
                //     title: false,
                //     area: ['400px', '200px'],
                //     offset: ["28%", "20%"],
                //     closeBtn: 0,
                //     shadeClose: false,
                //     scrollbar: false,
                //     skin: 'myclas',
                //     content: '<div style="width:350px;margin:auto;margin-top:100px;font-size:20px;">邮件发送成功，请查收！<a style="color:#fecc2f" href="/login/">点击返回登录</a></div>'
                // });
            }

        }
    });


}

function activefail() {
    layer.closeAll();
    layer.open({
        type: 1,
        title: false,
        area: ['400px', '200px'],
        offset: ["28%", "20%"],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'myclas',
        content: '<div style="width:350px;margin:auto;margin-top:100px;font-size:20px;">链接已经失效，请重新获取！<a style="color:#fecc2f" href="/forget/">点击返回</a></div>'
    });
}

function password_reset(obj, type) {
    layer.closeAll();
    layer.open({
        type: 1,
        title: false,
        area: ['500px', '300px'],
        offset: ["28%", "20%"],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'myclas',
        content: '            <div id="page-change-pwd" style="position:relative;display: block;">\n' +
        '\n' +
        '                <div class="comment_section" style="width: 490px;padding: 22px 22px;min-height: 280px">\n' +
        '                    <div style="position: relative;">\n' +
        '                        <p class="head-title">重置密码</p>\n' +
        '                    </div>\n' +
        '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
        '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n' +
        '                    <form id="reset-pwd-form" style="text-align: center">\n' +
        '<input type="hidden" name="obj" value="' + obj + '">' +
        '                        <input type="hidden" name="type" value="' + type + '">' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">新密码:</span>\n' +
        '                            <input id="password" type="password" name="password"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px;    padding-right: 27px;">\n' +
        '                            <span class="label_sbs">确认新密码:</span>\n' +
        '                            <input id="confirmPassword" type="password" name="confirmPassword"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +
        '                        <div id="resetpwdbtn" onclick="resetpwd()" style="margin-top: 24px" class="small_btn">提交</div>\n' +
        '                    </form>\n' +
        '                </div>\n' +
        '\n' +
        '            </div>'
    });
}

function resetpwd() {
    if ($("#confirmPassword").val() != $("#password").val()) {
        alert('密码不一致');
        $("#confirmPassword").css("border", "1px solid red");
        return false;
    }
    if ($("#password").val() == "") {
        alert('新密码不能为空');
        return false;
    }
    $.ajax({
        cache: false,
        type: "POST",
        dataType: 'json',
        url: "/modify_pwd/",
        data: $('#reset-pwd-form').serialize(),
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            if (data.msg == 'fail') {
                layer.tips(data.msg, $("#resetpwdbtn"));
            }
            else {
                layer.tips('密码重置成功，返回登录', $("#resetpwdbtn"));
                window.location.href = '/login/';
            }
        }
    });
}


function popregister_mobile() {
    layer.closeAll();
    layer.open({
        type: 1,
        title: false,
        area: ['500px', '400'],
        offset: ["28%", "20%"],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'myclas',
        content: '' +
        '\n' +
        '                <div class="comment_section" style="padding: 22px 22px;min-height: 250px">\n' +
        '                    <div style="position: relative;text-align: center;">\n' +
        '                        <p class="head-title"><span onclick="popregister_mobile()" class="mytab active">手机注册</span><span onclick="popregister_email()" class="mytab" style="margin-left: 20px">邮箱注册</span></p>\n' +
        '                    </div>\n' +
        '                    <form id="register-form-mobile" style="text-align: center">\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">手机号:</span>\n' +
        '                            <input id="mobile" type="tel" name="mobile" placeholder="请输入手机号"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">验证码:</span>\n' +
        '                            <input id="verify_code" type="text" maxlength="4" name="verify_code" autocomplete="off" placeholder="请输入验证码"\n' +
        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px"> <img id="code" style="width: 100px;\n' +
        '    height: 35px;" onclick="refresh_code(this)" src="/users/verify_code/">\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px;    padding-right: 27px;">\n' +
        '                            <span class="label_sbs">短信验证码:</span>\n' +
        '                            <input id="sms_code" type="text" maxlength="4" name="sms_code"\n' +
        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px">' +
        '<div id="get_sms_code" onclick="get_sms_code(this,\'register\')" class="smscode">获取验证码</div>\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px;    padding-left: 13px;">\n' +
        '                            <span class="label_sbs">密码:</span>\n' +
        '                            <input id="password" type="password" name="password" placeholder="请输入您的密码"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +

        '                        <div id="register" onclick="register(\'mobile\')" style="margin-top: 24px" class="small_btn">立即注册</div>\n' +
        '                    </form>\n' +
        '  <div class="label_sbs" style="margin-top:20px;text-align: center;padding-left: 55px;"><span>已有账号?</span><span class="btnoff"><a style="color: red" href="/login">立即登录</a></span><span class="btnoff"><a style="color: red" href="/forget">忘记密码</a></span><span class="btnoff" style="color: red"><a style="color: red" href="/">回到首页</a></span></div>                                      ' +
        '                </div>\n'
    });
    $("#verify_code").html("");
    refresh_code($("#code"));

}

function popregister_email() {
    layer.closeAll();
    layer.open({
        type: 1,
        title: false,
        area: ['500px', '400'],
        offset: ["28%", "20%"],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'myclas',
        content: '' +
        '\n' +
        '                <div class="comment_section" style="padding: 22px 22px;min-height: 250px">\n' +
        '                    <div style="position: relative;text-align: center;">\n' +
        '                        <p class="head-title"><span onclick="popregister_mobile()" class="mytab ">手机注册</span><span onclick="popregister_email()" class="mytab active" style="margin-left: 20px">邮箱注册</span></p>\n' +
        '                    </div>\n' +
        '                    <form id="register-form-email" style="text-align: center">\n' +
        '                        <div style="margin-top: 20px;padding-left: 13px;">\n' +
        '                            <span class="label_sbs">邮箱:</span>\n' +
        '                            <input id="email" type="email" name="email" placeholder="请输入邮箱"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">验证码:</span>\n' +
        '                            <input id="verify_code" type="text" maxlength="4" name="verify_code" autocomplete="off" placeholder="请输入验证码"\n' +
        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px"> <img id="code" style="width: 100px;\n' +
        '    height: 35px;" onclick="refresh_code(this)" src="/users/verify_code/">\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px;    padding-right: 27px;">\n' +
        '                            <span class="label_sbs">邮箱验证码:</span>\n' +
        '                            <input id="email_code" type="text" maxlength="4" name="email_code"\n' +
        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px">' +
        '<div id="get_email_code" onclick="get_email_code(this,\'register\')" class="smscode">获取验证码</div>\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px;    padding-left: 13px;">\n' +
        '                            <span class="label_sbs">密码:</span>\n' +
        '                            <input id="password" type="password" name="password" placeholder="请输入您的密码"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +

        '                        <div id="register" onclick="register(\'email\')" style="margin-top: 24px" class="small_btn">立即注册</div>\n' +
        '                    </form>\n' +
        '  <div class="label_sbs" style="margin-top:20px;text-align: center;padding-left: 55px;"><span>已有账号?</span><span class="btnoff"><a style="color: red" href="/login">立即登录</a></span><span class="btnoff"><a style="color: red" href="/forget">忘记密码</a></span><span class="btnoff" style="color: red"><a style="color: red" href="/">回到首页</a></span></div>                                      ' +
        '                </div>\n'
    });
    $("#verify_code").html("");
    refresh_code($("#code"));

}


function poplogin(enabel_close) {
    enabel_close = typeof enabel_close !== 'undefined' ? enabel_close : false;
    if (enabel_close) {
        closestr = '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
            '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n';
        headtitle = '                        <p style="padding-right: 22px" class="head-title">需登录账号</p>\n';
    } else {
        closestr = '';
        headtitle = '                        <p class="head-title">账号登录</p>\n';
    }
    layer.open({
        type: 1,
        title: false,
        area: ['500px', '370px'],
        offset: ["28%", "20%"],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'myclas',
        content: '' +
        '\n' +
        '                <div class="comment_section" style="padding: 22px 22px;min-height: 250px">\n' +
        '                    <div style="position: relative;text-align: right;">\n' +
        '<img width="41px" height="41px" style="position: absolute; left:0; top: -10px"\n' +
        '                             src="/static/demo/images/LOGO_new.png"/>\n' +
        '                        <img height="41px" style="position: absolute; left:50px; top: -10px"\n' +
        '                             src="/static/demo/images/logo_text.png"/>' + headtitle +
        '                    </div>\n' + closestr +
        '                    <form id="login-form" style="text-align: center">\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">用户名:</span>\n' +
        '                            <input id="username" type="text" name="username" placeholder="手机号/邮箱"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px;    padding-left: 13px;">\n' +
        '                            <span class="label_sbs">密码:</span>\n' +
        '                            <input id="password" type="password" name="password" placeholder="请输入您的密码"\n' +
        '                                   style=" width: 216px; padding-left: 11px; margin-left: 10px">\n' +
        '                        </div>\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                            <span class="label_sbs">验证码:</span>\n' +
        '                            <input id="verify_code" type="text" maxlength="4" name="verify_code" autocomplete="off" placeholder="请输入验证码"\n' +
        '                                   style=" width: 113px; padding-left: 11px; margin-left: 10px"> <img id="code" style="width: 100px;\n' +
        '    height: 35px;" onclick="refresh_code(this)" src="/users/verify_code/">\n' +
        '                        </div>\n' +
        '                        <div id="login" onclick="login()" style="margin-top: 24px" class="small_btn">立即登录</div>\n' +
        '                    </form>\n' +
        '  <div class="label_sbs" style="margin-top:20px;text-align: center;padding-left: 55px;"><span>没有账号?</span><span class="btnoff"><a style="color: red" href="/register">立即注册</a></span><span class="btnoff"><a style="color: red" href="/forget">忘记密码</a></span><span class="btnoff" style="color: red"><a style="color: red" href="/">回到首页</a></span></div>                                      ' +
        '                </div>\n'
    });
    $("#verify_code").html("");
    //绑定回车键
    $("input").bind("keypress", function (event) {
        if (event.keyCode == "13") {
            login();
        }
    });


}

function popBuyVIP(enabel_close) {
    enabel_close = typeof enabel_close !== 'undefined' ? enabel_close : false;
    if (enabel_close) {
        closestr = '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
            '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n';
        headtitle = '                        <p style="padding-right: 22px" class="head-title">购买VIP</p>\n';
    } else {
        closestr = '';
        headtitle = '                        <p class="head-title">购买VIP</p>\n';
    }
    layer.open({
        type: 1,
        title: false,
        area: ['500px', '350px'],
        offset: ["28%", "20%"],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'myclas',
        content: '' +
        '\n' +
        '                <div class="comment_section" style="padding: 22px 22px;min-height: 250px">\n' +
        '                    <div style="position: relative;text-align: left;">\n' +
        '' + headtitle +
        '                    </div>\n' + closestr +
        '                    <form id="login-form" style="text-align: center">\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                           <div><img  src="/static/images/vip.png"/></div>\n<div style="margin-top: 22px;" class="label_sbs">当前权限无法查看资料，请购买VIP</div>' +
        // '                        <div onclick="window.location=\'/trades/buy/vip/0\'" style="margin-top: 24px;margin-left: 0px" class="small_btn">立即开通VIP服务</div>\n' +
        '                        <div onclick="alert(\'线上购买功能暂未开放，敬请期待！\')" style="margin-top: 24px;margin-left: 0px" class="small_btn">立即开通VIP服务</div>\n' +
        '                    </form>\n' +
        '                </div>\n'
    });
    $("#verify_code").html("");

}

function popBuyCourse(enabel_close) {
    enabel_close = typeof enabel_close !== 'undefined' ? enabel_close : false;
    if (enabel_close) {
        closestr = '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
            '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n';
        headtitle = '                        <p style="padding-right: 22px" class="head-title">购买课程</p>\n';
    } else {
        closestr = '';
        headtitle = '                        <p class="head-title">购买课程</p>\n';
    }
    layer.open({
        type: 1,
        title: false,
        area: ['500px', '350px'],
        offset: ["28%", "20%"],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'myclas',
        content: '' +
        '\n' +
        '                <div class="comment_section" style="padding: 22px 22px;min-height: 250px">\n' +
        '                    <div style="position: relative;text-align: left;">\n' +
        '' + headtitle +
        '                    </div>\n' + closestr +
        '                    <form id="login-form" style="text-align: center">\n' +
        '                        <div style="margin-top: 20px">\n' +
        '                           <div><img  src="/static/images/vip.png"/></div>\n<div style="margin-top: 22px;" class="label_sbs">您没有任何课程！</div>' +
        '                        <div onclick="window.location=\'/course/list/\'" style="margin-top: 24px;width120px;margin-left: 0px" class="small_btn">立即报课</div>\n' +
        '                    </form>\n' +
        '                </div>\n'
    });
    $("#verify_code").html("");

}

function popAuth(enabel_close) {
    enabel_close = typeof enabel_close !== 'undefined' ? enabel_close : false;
    if (enabel_close) {
        closestr = '                    <img class="layui-layer-close layui-layer-close2" id="closebtn"\n' +
            '                         style="position: absolute;right: 22px; top: 30px;" src="/static/demo/images/close.png">\n';
        headtitle = '                        <p style="padding-right: 22px" class="head-title">抱歉，您没有权限查看此内容！</p>\n';
    } else {
        closestr = '';
        headtitle = '                        <p class="head-title">抱歉，您没有权限查看此内容！</p>\n';
    }
    layer.open({
        type: 1,
        title: false,
        area: ['500px', '400px'],
        offset: ["28%", "20%"],
        closeBtn: 0,
        shadeClose: false,
        scrollbar: false,
        skin: 'myclas',
        content: '' +
        '\n' +
        '                <div class="comment_section" style="padding: 22px 22px;min-height: 250px">\n' +
        '                    <div style="position: relative;text-align: left;">\n' +
        '' + headtitle +
        '                    </div>\n' + closestr +
        '                    <form id="login-form" style="text-align: center">\n' +
        '                        <div style="margin-top: 20px">\n' +
        '<div><a style="font-size: 20px" href="/hotfeatures" target="_blank">用户权限一览</a></div>' +
        '<div>课程报名/咨询，</div>' +
        '<div>请联系微信公众号gu_stepbystep</div>' +
        '                           <div><img src="/static/demo/images/sbs_weixin.jpg" height="120px" /></div>\n' +
        '<div>早上9:00-晚22:30为您服务！</div>' +
        '                    </form>\n' +
        '                </div>\n'
    });
    $("#verify_code").html("");

}

function login() {

    if ($("#username").val() == "") {
        layer.tips('用户名不能为空', $("#username"));
        $("#username").css("border", "1px solid red");
        return false;
    }
    if ($("#verify_code").val() == "") {
        layer.tips('图形验证码不能为空', $("#verify_code"));
        $("#verify_code").css("border", "1px solid red");
        return false;
    }
    if ($("#password").val() == "") {
        layer.tips('密码不能为空', $("#password"));
        $("#sms_code").css("border", "1px solid red");
        return false;
    }

    $.ajax({
        cache: false,
        type: "POST",
        dataType: 'json',
        url: "/login/",
        data: $('#login-form').serialize(),
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            if (data.status == "fail") {
                layer.tips(data.msg, $("#login"));
                refresh_code("#code");
                return false;

            }
            else {
                layer.closeAll();
                if (window.location.href.indexOf('login') > -1) {
                    window.location.href = data.next;
                } else {
                    window.location.reload();
                }

            }

        }
    });


}


function register(type) {

    var url = "";
    var data;
    if (type == "mobile") {

        url = "/register_phone/";
        data = $('#register-form-mobile').serialize();

        if ($("#mobile").val() == "") {
            layer.tips('手机号不能为空', $("#mobile"));
            $("#mobile").css("border", "1px solid red");
            return false;
        }
        if ($("#sms_code").val() == "") {
            layer.tips('短信验证码不能为空', $("#sms_code"));
            $("#sms_code").css("border", "1px solid red");
            return false;
        }
    } else if (type == "email") {
        url = "/register/";
        data = $('#register-form-email').serialize();
        if ($("#email").val() == "") {
            layer.tips('邮箱不能为空', $("#email"));
            $("#email").css("border", "1px solid red");
            return false;
        }
        if ($("#email_code").val() == "") {
            layer.tips('邮箱验证码不能为空', $("#email_code"));
            $("#email_code").css("border", "1px solid red");
            return false;
        }
    } else {
        return false;
    }
    if ($("#verify_code").val() == "") {
        layer.tips('图形验证码不能为空', $("#verify_code"));
        $("#verify_code").css("border", "1px solid red");
        return false;
    }
    if ($("#password").val() == "") {
        layer.tips('密码不能为空', $("#password"));
        $("#sms_code").css("border", "1px solid red");
        return false;
    }


    $.ajax({
        cache: false,
        type: "POST",
        dataType: 'json',
        url: url,
        data: data,
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        },
        success: function (data) {
            if (data.status == "fail") {
                layer.tips(data.msg, $("#register"));
                refresh_code("#code");
                return false;

            }
            else {
                layer.closeAll();
                window.location.href = "/users/info/";
            }

        }
    });


}
