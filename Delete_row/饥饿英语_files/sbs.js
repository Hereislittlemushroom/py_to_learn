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

function msgBlink() {
    if ($('#message').hasClass('blink')) {
        $('#message').removeClass('blink');
    } else {
        $('#message').addClass('blink');
    }
}

var MessageAlert = function () {
    var msg = parseInt($('#message').data('msg'));
    if (msg > 0) {
        setInterval(msgBlink, 300);
    }
}

var FormatMp3 = function () {

    $('a[href$=".mp3"]').each(function () {
        //删除图标
        var mp3dom = $(this);
        var imgdom = $(this).prev();
        if ($(imgdom).attr('src').indexOf('icon_mp3.gif') > -1) {
            $(imgdom).remove();
            var title = $(mp3dom).text();
            var src = $(mp3dom).attr('href');
            var audio = $('<audio controls="controls"><source src="' + src + '"  type="audio/mp3"/></audio>');
            $(mp3dom).after($(audio));
            $(mp3dom).remove();
        }
    });
};
var SetCommentUrl = function () {
    var url = window.location.pathname;
    $('input[name="comment_url"]').attr('value', url);
};
(function ($) {
    $.fn.textSearch = function (str, options) {
        var defaults = {
            divFlag: true,
            divStr: " ",
            markClass: "highlight",
            markColor: "",
            nullReport: false,
            callback: function () {
                return false;
            }
        };
        var sets = $.extend({}, defaults, options || {}), clStr;
        if (sets.markColor) {
            clStr = "style='color:" + sets.markColor + ";'";

        } else {
            clStr = "class='" + sets.markClass + "'";
        }

        //对前一次高亮处理的文字还原
        $("span[rel='mark']").each(function () {
            var text = document.createTextNode($(this).text());
            $(this).replaceWith($(text));
        });


        //字符串正则表达式关键字转化
        $.regTrim = function (s) {
            var imp = /[\^\.\\\|\(\)\*\+\-\$\[\]\?]/g;
            var imp_c = {};
            imp_c["^"] = "\\^";
            imp_c["."] = "\\.";
            imp_c["\\"] = "\\\\";
            imp_c["|"] = "\\|";
            imp_c["("] = "\\(";
            imp_c[")"] = "\\)";
            imp_c["*"] = "\\*";
            imp_c["+"] = "\\+";
            imp_c["-"] = "\\-";
            imp_c["$"] = "\$";
            imp_c["["] = "\\[";
            imp_c["]"] = "\\]";
            imp_c["?"] = "\\?";
            s = s.replace(imp, function (o) {
                return imp_c[o];
            });
            return s;
        };

        var t = $(this);
        str = $.trim(str);
        if (str === "") {
            alert("关键字为空");
            return false;
        } else {
            //将关键字push到数组之中
            var arr = [];
            if (sets.divFlag) {
                arr = str.split(sets.divStr);
            } else {
                arr.push(str);
            }
        }
        var v_html = t.html();
        //删除注释
        v_html = v_html.replace(/ <!--(?:.*)\-->/g, "");

        //将HTML代码支离为HTML片段和文字片段，其中文字片段用于正则替换处理，而HTML片段置之不理
        var tags = /[^<>]+|<(\/?)([A-Za-z]+)([^<>]*)>/g;
        var a = v_html.match(tags), test = 0;
        $.each(a, function (i, c) {
            if (!/<(?:.|\s)*?>/.test(c)) {//非标签
                //开始执行替换
                $.each(arr, function (index, con) {
                    if (con === "") {
                        return;
                    }
                    var reg = new RegExp($.regTrim(con), "gi");
                    if (reg.test(c)) {
                        //正则替换
                        var reg1 = new RegExp($.regTrim(con), "gi");
                        var otext = reg1.exec(c);
                        c = c.replace(reg, "♂" + otext + "♀");
                        test = 1;
                    }
                });
                c = c.replace(/♂/g, "<span " + clStr + ">").replace(/♀/g, "</span>");
                a[i] = c;
            }
        });
        //将支离数组重新组成字符串
        var new_html = a.join("");

        $(this).html(new_html);

        if (test === 0 && sets.nullReport) {
            alert("没有搜索结果");
            return false;
        }
        //执行回调函数
        sets.callback();
        if (test === 0) {
            return false;
        } else {
            return true;

        }

    };
})(jQuery);

(function ($) {
    $.fn.pageList = function (options) {
        var defaults = {
            list_id: '',
            current_page: 0,
            page_size: 0,
            request_url: '',
            filter: '',
            select_id: '',
            select_filed: '',
            custom_param: '',
            has_comments: true,
            select_filter: '',
            load_firsttme: true,
            total: 0,
            callback: function () {
                return false;
            },
            custom_callback: function () {
                return false;
            }
        };

        //绑定翻页
        var bindEvent = function () {
            // $('.pagenum').each(function () {
            //     this.onclick = go_current;
            // });
            $('#' + sets.list_id + '_page_previous').siblings().each(function () {
                if ($(this).attr("id") == undefined) {
                    this.onclick = go_current;
                }
            });
            $('#' + sets.list_id + '_page_previous')[0].onclick = go_previous;
            $('#' + sets.list_id + '_page_next')[0].onclick = go_next;
        };

        //搜索框
        var search_page = function () {
            if (sets.select_filed == '' || sets.select_id == '') {
                sets.has_select = '';
                return;
            }
            var select_val = $('#' + sets.select_id + '').val();
            if (select_val == '' || select_val == null) {
                sets.select_filter = '';
                reload_pagelist();
                return;
            }
            sets.select_filter = '&' + sets.select_filed + '=' + select_val;
            reload_pagelist();
        };

        //清除搜索
        var clear_search = function () {
            $("#" + sets.select_id).val('');
            sets.select_filter = '';
            reload_pagelist();
        };

        //设置页脚
        var set_page = function () {
            var j = 0;
            var list_id = sets.list_id;
            var total = sets.total;
            if (sets.current_page == 1) {
                $('#' + list_id + '_page_previous').addClass("disabled");
            }
            else {
                $('#' + list_id + '_page_previous').removeClass("disabled");
            }
            if (sets.current_page == total + 1) {
                $('#' + list_id + '_page_next').addClass("disabled");
            }
            else {
                $('#' + list_id + '_page_next').removeClass("disabled");
            }
            if (total <= 4) {
                for (j = total; j >= 0; j--) {
                    if (j == (sets.current_page - 1)) {
                        $('#' + list_id + '_page_previous').after('<li class="active"><a class="pagenum btnum">' + (j + 1) + '</a></li>');
                    }
                    else {
                        $('#' + list_id + '_page_previous').after('<li><a class="pagenum btnum">' + (j + 1) + '</a></li>');
                    }
                }
            }
            else if (sets.current_page <= 3) {
                for (j = 4; j >= 0; j--) {
                    if (j == (sets.current_page - 1)) {
                        $('#' + list_id + '_page_previous').after('<li class="active"><a class="pagenum btnum">' + (j + 1) + '</a></li>');
                    }
                    else {
                        $('#' + list_id + '_page_previous').after('<li><a class="pagenum btnum">' + (j + 1) + '</a></li>');
                    }
                }
            }
            else if (sets.current_page >= total - 1) {
                for (j = total; j >= total - 4; j--) {
                    if (j == (sets.current_page - 1)) {
                        $('#' + list_id + '_page_previous').after('<li class="active"><a class="pagenum btnum">' + (j + 1) + '</a></li>');
                    }
                    else {
                        $('#' + list_id + '_page_previous').after('<li><a class="pagenum btnum">' + (j + 1) + '</a></li>');
                    }
                }
            }
            else {
                for (j = sets.current_page + 1; j >= sets.current_page - 3; j--) {
                    if (j == (sets.current_page - 1)) {
                        $('#' + list_id + '_page_previous').after('<li class="active"><a class="pagenum btnum">' + (j + 1) + '</a></li>');
                    }
                    else {
                        $('#' + list_id + '_page_previous').after('<li><a class="pagenum btnum">' + (j + 1) + '</a></li>');
                    }
                }
            }

            bindEvent();
        };

        //初始化页脚
        var load_paginate = function () {
            var page_content = '                    <nav aria-label="Page navigation" style="float:right;margin-right:-10px">\n' +
                '                        <ul class="pagination" id="comment_page">\n' +
                '                            <li class="disabled" id="' + sets.list_id + '_page_previous">\n' +
                '                                <a aria-label="Previous" class="btaction">\n' +
                '                                    <span aria-hidden="true" style="font-size: 12px; margin: 0 ">上一页</span>\n' +
                '                                </a>\n' +
                '                            </li>\n' +
                '\n' +
                '                            <li id="' + sets.list_id + '_page_next">\n' +
                '                                <a aria-label="Next" class="btaction">\n' +
                '                                    <span aria-hidden="true" style="font-size: 12px; margin: 0">下一页</span>\n' +
                '                                </a>\n' +
                '                            </li>\n' +
                '                        </ul>\n' +
                '                    </nav>';
            $('#' + sets.list_id).after(page_content);
        };

        //重新加载数据
        var reload_pagelist = function () {
            var l_id = sets.list_id;
            $('#' + l_id + ' li').remove();
            //$('a.pagenum').remove();
            $('#' + l_id).siblings('nav').children('ul').children('li').children('.pagenum').remove();
            var url = sets.request_url.split('?')[0];
            sets.request_url = url + '?page_size=' + sets.page_size + '&page=' + sets.current_page;
            getCommentList();
        };

        //上一页、下一页和跳转到指定页面
        var go_previous = function () {
            if ($(this).attr("class") == "disabled" || sets.has_comments == 0) {
                return;
            }
            sets.current_page = sets.current_page - 1;
            reload_pagelist();
        };

        var go_next = function () {
            if ($(this).attr("class") == "disabled" || sets.has_comments == 0) {
                return;
            }
            sets.current_page = sets.current_page + 1;
            reload_pagelist();
        };

        var go_current = function () {
            var pagenum = parseInt($(this).text());
            if (pagenum == sets.current_page || sets.has_comments == 0) {
                return;
            }
            sets.current_page = pagenum;
            reload_pagelist();
        };

        //请求数据
        var getCommentList = function () {
            $.ajax({
                type: 'GET',
                url: sets.request_url + sets.filter + sets.select_filter + sets.custom_param,
                dataType: 'json',
                beforeSend: function (xhr, settings) {
                    xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
                },
                success: function (data) {
                    if (data.results.length > 0) {
                        sets.has_comments = 1;
                        var total = parseInt((data.count - 1) / sets.page_size);
                        sets.total = total;
                        set_page();

                        for (var i = 0; i < data.results.length; i++) {
                            var info = data.results[i];
                            var li_content = sets.callback(info);
                            if (li_content != null && li_content != '') {
                                $('#' + sets.list_id).append(li_content);
                            }
                        }
                        if (typeof(sets.custom_callback) != "undefined") {
                            sets.custom_callback();
                        }
                    }
                    else {
                        sets.has_comments = 0;
                        $('#' + sets.list_id).append("<li>暂无数据！</li>");
                    }

                },
                error: function (xhr, textStatus) {
                    console.log(xhr);
                    console.log(textStatus);
                }
            })
        };

        //初始化页面
        var sets = $.extend({}, defaults, options || {});
        load_paginate();
        if (sets.load_firsttme) {
            getCommentList();
        }
        else {
            set_page();
        }
        //初始化搜索框
        if (sets.select_filed != '' && sets.select_id != '') {
            $("#" + sets.select_id).siblings('.search-icon')[0].onclick = search_page;
            $("#" + sets.select_id).siblings('.close-icon')[0].onclick = clear_search;
            $("#" + sets.select_id).bind("keypress", function (event) {
                if (event.keyCode == "13") {
                    search_page();
                }
            });
        }
    };
})(jQuery);

var SearchManager = function () {
    this.init();
};
SearchManager.prototype.init = function () {
    this.bindEvent();
};
SearchManager.prototype.startSearch = function (btn) {

    function searchTarget(searchtext, targetElement) {
        var flag = $(targetElement).textSearch(searchtext, {
            markClass: "highlight", callback: function () {
                return true;
            }
        });
        console.log(flag);
        return flag;
    }

    var is_searched = false;
    var firstshow = false;
    var parent = $(btn).parent().parent().parent();
    var keyword = $(parent).find('.search-box').val();
    if (keyword == "") {
        return false;
    }
    //隐藏所有一级选项
    $(parent).children(".first_category").children("ul").children("li").hide();
    //隐藏所有二级选项
    $(parent).children(".second_category").hide();

    $(parent).children(".second_category").each(function (index, element) {
        if (!$(element)) {
            return false;
        }
        $(element).removeClass('highlight');
        //清除之前搜索高亮的记录
        $(element).find('*').each(function () {
            $(this).removeClass('highlight');
        });

        var flag = false;
        flag = searchTarget(keyword, element);
        if (flag) {
            is_searched = true;
            var mask = $(parent).find('.non-mask').hide();
            $(parent).children(".first_category").children("ul").children("li").eq(index).css("display", 'block');
            if (!firstshow) {
                $(element).show();
                firstshow = true;
            }
        }
        if (!is_searched) {
            var mask = $(parent).find('.non-mask');
            if ($(mask).css('display') == "none") {
                $(mask).show();
            }
        }
    });
    $(parent).children(".first_category").niceScroll().resize();

};
SearchManager.prototype.clearSearch = function (btn) {
    var parent = $(btn).parent().parent().parent();
    //显示所有1级
    $(parent).children(".first_category").children("ul").children("li").show();
    $(parent).children(".second_category").each(function (index, element) {
        if (!$(element)) {
            return false;
        }
        $(element).removeClass('highlight');
        //清除之前搜索高亮的记录
        $(element).find('*').each(function () {
            $(this).removeClass('highlight');
        });
    });
    $(parent).children(".second_category").hide();
    $(parent).children(".second_category").eq(0).show();

    //隐藏哭脸
    $(parent).children(".non-mask").hide();
};
SearchManager.prototype.bindEvent = function () {
    var that = this;
    //输入框回车键
    $('.search-box').bind("keypress", function (event) {
        if (event.keyCode == "13") {
            that.startSearch($(this));
        }
    });

    $('.search-box').on('input', function () {
        if ($(this).val() == '' || $(this).val() == null) {
            that.clearSearch($(this));
        }
    });

    $('.search-icon').click(function () {
        that.startSearch($(this));
    });
    //清空搜索框
    $('.close-icon').click(function () {
        $(this).prev().prev().val('');
        $(this).hide();
        that.clearSearch($(this));
    });
};

function registerPigai() {
    $(".pigai").click(function () {
        $(".pigai").toggleClass("checked");
    });
}

function SbsMp3Recorder(params) {
    var allblob = [];
    var is_recording = false;
    var current_recording_testid = null;
    var current_recording_type = null;
    var typeURlMap = params.typeURL || null;

    function init() {
        is_recording = false;
        recorder = new MP3Recorder({
            debug: false,
            funOk: function () {
                console.log('录音初始化成功');
            },
            funCancel: function (msg) {
                console.log(msg);
                // alert("为保证录音成功，建议您使用Chrome浏览器！");
                recorder = null;
            }
        });
        mp3Blob = null;
    }

    function saveBlob(type, testid, blob) {
        if (!allblob[type]) {
            allblob[type] = [];
        }
        allblob[type][testid] = blob;
    }

    function saveRecordingMp3() {
        is_recording = false;
        var tmp_testid = current_recording_testid || null;
        var tmp_type = current_recording_type || null;
        console.log('正在录音，停止录音');
        recorder.stop();
        recorder.getMp3Blob(function (blob) {
            //log('MP3导出成功');
            if (tmp_testid && tmp_type) {
                saveBlob(tmp_type, tmp_testid, blob);
            }
            //填充至正在录制的recordinglist中
            var url = URL.createObjectURL(blob);
            var div = $('<div></div>');
            var au = $('<audio></audio>');

            au.attr('controls', true);
            au.attr('src', url);
            div.append(au);
            var root = $('.luyin[data-type="' + tmp_type + '"][data-testid="' + tmp_testid + '"]').parent();
            $(root).find('.recordingslist').append(div);
            //上传按钮中设置type和id
            $(root).find('.btnUpload').data('type', tmp_type);
            $(root).find('.btnUpload').data('testid', tmp_testid);
            $(root).children('.myanswer').show();
            $(root).children('.box-upload').show();
            $('.second_category').niceScroll().resize();
        });
    }

    function bindEvent() {
        //开始录音
        $('.luyin').click(function () {

            var type = $(this).data("type");
            var testid = $(this).data("testid");
            if (is_recording) {
                saveRecordingMp3();
                $('.luyin').show();
                $('.guocheng').hide();
                //
            }
            console.log('start', "type:", type, "testid:", testid);
            $(this).attr('disabled', true);
            try {
                recorder.start();
            }
            catch (e) {
                alert("为保证录音成功，建议您使用Chrome浏览器！");
                return;
            }
            is_recording = true;
            current_recording_testid = testid;
            current_recording_type = type;
            var root = $(this).parent();
            $(root).children('.luyin').hide();
            $(root).children('.myanswer').hide();
            //开始录音，清空已有的录音
            $(root).find('.recordingslist').html("");
            $(root).children('.box-upload').hide();
            $(root).children('.guocheng').show();
        });
        //停止录音
        $('.guocheng').click(function () {
            saveRecordingMp3();
            //log('录音结束，MP3导出中...');
            var root = $(this).parent();
            $(root).find('.luyin-label').html("点击重新开始录音");
            $(root).children('.luyin').show();
            $(root).children('.myanswer').show();
            $(root).children('.box-upload').show();
            $(root).children('.box-upload').children('input').show();
            $(root).children('.guocheng').hide();

        });
        //上传录音
        $('.btnUpload').click(function () {
            var type = $(this).data('type');
            var testid = $(this).data('testid');
            var url = typeURlMap[type];
            var fd = new FormData();

            var need_pg = $(this).parent().find('.pigai').hasClass("checked");
            if (need_pg) {
                fd.append('needReply', 'Y');
            }
            fd.append('testid', testid);
            fd.append('file', allblob[type][testid]);

            var _this = this;

            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    var data = eval('(' + xhr.responseText + ')');
                    console.log(data);
                    if (data.status == "success") {
                        alert('答案上传成功!');
                        if (need_pg) {
                            $(_this).siblings('.buypigai').remove();
                            var times = 0;
                            try {
                                times = parseInt($(_this).siblings('.pigai').children().text().trim());
                                times--;
                            }
                            catch (e) {

                            }
                            $(_this).siblings('.pigai').replaceWith('<div class="checked buypigai">已申请批改</div>');
                            try {
                                $(".pigaitimes").each(function () {
                                    // var times = parseInt($(this).text().trim());
                                    // times--;
                                    $(this).text(times);
                                    if (times <= 0) {
                                        $('.pigai').hide();
                                        $('.buypigai').show();
                                    }
                                })
                            }
                            catch (e) {

                            }
                        }
                        // $(_this).hide();
                    } else {
                        if (data.reason == 'login') {
                            alertAuth(_this, 1);
                        }
                    }
                    //recordingslist.innerHTML += '上传成功：<a href="' + data.audiopath + '" >' + mp3Name + '</a>';
                }
            };
            xhr.open('POST', url);
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            xhr.send(fd);
        });
        //绑定批改按钮
        $(".pigai").click(function () {
            $(this).toggleClass("checked");
        });
    }

    //初始化mp3recorder
    init();
    bindEvent();
    return {
        getallblob: allblob
    };
}


var format = function (str) {
    if (parseInt(str) < 10) {
        return "0" + str;
    }
    return str;
};

function CountDownTimer(params) {
    var testvalue = 10;
    var hour = 0;
    var min = 0;
    var sec = 0;
    var idt = "";
    var alertinfor = "";
    var label = "";

    function init() {
        alertinfor = params.alert;
        min = params.min;
        label = params.label;
        $(label).text(format(hour) + ":" + format(min) + ":" + format(sec));
        if (min > 0 && min <= 60) {
            setCountDown_time();
        }

    };

    function setCountDown_time() {

        idt = window.setInterval(down, 1000);
        testvalue = 1000;
    };

    function down() {
        // console.log(hour, min, sec);
        sec--;
        if (sec <= 0) {
            if (parseInt(min) <= 0 && parseInt(sec) <= 0 && parseInt(hour) <= 0) {
                $(label).text(format(hour) + ":" + format(min) + ":" + format(sec));
                window.clearInterval(idt);
                alert(alertinfor + '作答时间到，请注意控制答题时间！');
            } else if (parseInt(min) <= 0 && parseInt(sec) <= 0) {
                hour--;
                min = 59;
                sec = 59;
            } else {
                min--;
                sec = 59;
            }
        }
        $(label).text(format(hour) + ":" + format(min) + ":" + format(sec));

    };

    function stopTimer() {
        window.clearInterval(idt);
    }

    init();
    return {
        stopTimer: stopTimer
    };
}


var SmallNavi = {
    Offset: 100,
    init: function (params) {
        if (params) {
            SmallNavi.Offset = params.offset || 0;
        }
        SmallNavi.setSectionIDs();
        SmallNavi.resetSmallMenuPosition();
        SmallNavi.bindEnvent();
    },
    setSectionIDs: function () {
        $('.small_menu').hide();
        $('.section-target-fix').each(function (index) {
            $(this).attr('id', 'section' + index);
            $('<a href="#section' + index + '"><div class="small_menu_title"><em class="pointer"></em><span  class="small_menu_title_word">' + $(this).attr('title') + '</span></div></a>').appendTo($('.small_menu'));

        });
        $('.small_menu').show();
        $('.circle').show();
        $('.bottom_circle').show();
        SmallNavi.HighlightCurrentNode();
        SmallNavi.resetSmallMenuHeight();
    },
    HighlightCurrentNode: function () {
        var wst = $(window).scrollTop() + SmallNavi.Offset;
        for (i = 0; i < $('.small_menu_title').length; i++) {
            if (!$('#section' + i).length > 0) {
                return false;
            }
            if ($('#section' + i).offset().top <= wst) {
                $('.small_menu_title').removeClass('small_menu_title_active');
                $('.small_menu_title').eq(i).addClass('small_menu_title_active');
            }
        }
    },
    resetSmallMenuHeight: function () {
        var target_height = $('.section-target-fix').length * 40 + 40;
        $('.small_menu').height(target_height);
    },
    resetSmallMenuPosition: function () {
        var height = window.innerWidth / 2 + 1016 / 2;
        $('.small_menu').css('left', height);
        $('.small_menu').css('left', height);
    },
    bindEnvent: function () {
        $(".bottom_circle").click(function () {
            $("html,body").animate({scrollTop: 0}, 500);
        });
        window.onresize = function () {
            SmallNavi.resetSmallMenuPosition();
        }
        $(window).scroll(function () {
            SmallNavi.HighlightCurrentNode();
        });
    },
}

var SmallNavi2 = {
    Offset: 100,
    init: function (params) {
        if (params) {
            SmallNavi2.Offset = params.offset || 100;
        }
        SmallNavi2.setSectionIDs();
        SmallNavi2.resetSmallMenuPosition();
        SmallNavi2.bindEnvent();
    },
    setSectionIDs: function () {
        $('.small_menu').hide();
        $('.section-target-fix').each(function (index) {
            $(this).attr('id', 'section' + index);
            $('<a href="#section' + index + '"><div class="small_menu_title"><em class="pointer"></em><span  class="small_menu_title_word">' + $(this).attr('title') + '</span></div></a>').appendTo($('.small_menu'));

        });
        SmallNavi2.resetSmallMenuHeight();
    },
    resetSmallMenuHeight: function () {
        var target_height = $('.section-target-fix').length * 40 + 40;
        $('.small_menu').height(target_height);
    },
    resetSmallMenuPosition: function () {
        var height = window.innerWidth / 2 + 1016 / 2;
        $('.small_menu').css('left', height + 50);
        // $('.small_menu').css('left', height);
    },
    bindEnvent: function () {
        $(".bottom_circle").click(function () {
            $("html,body").animate({scrollTop: 0}, 500);
        });
        window.onresize = function () {
            SmallNavi2.resetSmallMenuPosition();
        }
        $(window).scroll(function () {
            var wst = $(window).scrollTop() + SmallNavi2.Offset;
            if ($('#section1').offset().top <= wst) {
                $('.small_menu').show();
                $('.circle').show();
                $('.bottom_circle').show();

            } else {
                $('.small_menu').hide();
                $('.circle').hide();
                $('.bottom_circle').hide();

            }
            for (i = 0; i < $('.small_menu_title').length; i++) {
                if (!$('#section' + i).length > 0) {
                    return false;
                }
                if ($('#section' + i).offset().top <= wst) {
                    $('.small_menu_title').removeClass('small_menu_title_active');
                    $('.small_menu_title').eq(i).addClass('small_menu_title_active');
                }
            }
        });
    },
}


$('input.search-box').on('input', function () {
    if (this.value != null && this.value != "" && $(this).parent().children('.close-icon').css("display") == "none") {
        $(this).parent().children('.close-icon').show();
    }
    if ((this.value == null || this.value == "") && $(this).parent().children('.close-icon').css("display") != "none") {
        $(this).parent().children('.close-icon').hide();
    }
});


var UserLike = function (target, like_type, like_id, hint, attr, ok_icon, nok_icon) {

    $(target).click(function () {
        $.ajax({
            cache: false,
            type: 'post',
            dataType: 'json',
            url: "/api/v1/userLike/",
            data: {like_type: like_type, like_id: like_id},
            async: true,
            beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            },

            success: function (data, status) {

                if (data.msg == '点赞成功') {
                    alert(data.msg);
                    $(target).attr(attr, ok_icon);
                    new_num = parseInt($(target).next().html()) + 1;
                    $(target).next().html(new_num);


                } else {
                    // new_num = parseInt($(target).next().html()) - 1;
                    // if (new_num < 0) {
                    //     new_num = 0;
                    // }
                    // $(target).next().html(new_num);
                    // $(target).attr(attr, nok_icon);
                    alert(data.msg);
                }

            },
            error: function (data) {
                if (data.status == 400) {
                    alert("请先登录");
                }

            }
        });
    });

}

var TimeerDown = function (parentdiv, init_date) {
    var el_day = $(parentdiv).children(".day");
    var el_hour = $(parentdiv).children(".hour");
    var el_minute = $(parentdiv).children(".minute");
    var el_second = $(parentdiv).children(".second");

    function GetRTime() {
        var EndTime = new Date(init_date);
        var NowTime = new Date();
        var t = EndTime.getTime() - NowTime.getTime();
        var d = Math.floor(t / 1000 / 60 / 60 / 24);
        var h = Math.floor(t / 1000 / 60 / 60 % 24);
        var m = Math.floor(t / 1000 / 60 % 60);
        var s = Math.floor(t / 1000 % 60);

        el_day.html(d);
        el_hour.html(h);
        el_minute.html(m);
        el_second.html(s);
    }

    setInterval(GetRTime, 0);
}

//注册下拉事件
function registerScroll(parent) {

    $(parent).children(".first_category ").niceScroll({
        cursorcolor: "#fee1b2",
        cursoropacitymax: 1,
        touchbehavior: false,
        cursorwidth: "5px",
        railalign: "right",
        cursorborder: "0",
        autohidemode: false,
        cursorborderradius: "6px"

    });


    $(parent).children(".second_category").each(function () {
        $(this).niceScroll({
            cursorcolor: "#fee1b2",
            cursoropacitymax: 1,
            touchbehavior: false,
            cursorwidth: "5px",
            railalign: "right",
            cursorborder: "0",
            autohidemode: false,
            cursorborderradius: "5px"

        });

    });

}

//注册下拉事件
function registerScroll2(parent) {

    $(parent).children(".first_category ").niceScroll({
        cursorcolor: "#fee1b2",
        cursoropacitymax: 1,
        touchbehavior: false,
        cursorwidth: "5px",
        railalign: "right",
        cursorborder: "0",
        autohidemode: false,
        cursorborderradius: "6px"

    });

    $(parent).children(".second_category").each(function () {
        var target = $(this).children('.content');
        $(this).children('.content').niceScroll({
            cursorcolor: "#fee1b2",
            cursoropacitymax: 1,
            touchbehavior: false,
            cursorwidth: "5px",
            railalign: "right",
            cursorborder: "0",
            autohidemode: false,
            cursorborderradius: "5px"

        });
        $(target).getNiceScroll().resize();

    });

}

//注册点击事件
function registerClick(params) {
    var parent = params.parent;
    var enable_ids = params.enable_ids || null;
    var user_level = params.user_level || 1;
    var needLogin = params.needLogin || false;

    disableMouse($('.second_category'));
    $(parent).children(".first_category").children('ul').children('li').click(function () {
        if (needLogin) {
            if (user_level < 2) {
                alertAuth(this, user_level);
                return;
            }
        }
        if (params.hasPerm != undefined) {

            if (!params.hasPerm) {
                alertAuth("", user_level);
                return;
            }
        }
        var hasperm = $(this).data('hasperm');
        if (hasperm == "n") {
            alertAuth("", user_level);
            return;
        }
        index = parseInt($(this).attr("value"));
        model_id = parseInt($(this).data("model-id"));
        if (enable_ids) {
            if (!enable_ids.Exists(model_id)) {
                alertAuth("", user_level);
                return;
            }
        }

        $(this).parents(".syno_section").children(".second_category").hide();
        $(this).parents(".syno_section").children(".second_category").eq(index).css("display", 'block');
        $(this).siblings().removeClass("first_category_active");
        $(this).addClass("first_category_active");

    });
}

function disableMouse(btn) {
    // $(btn).mousedown(function (e) {
    //     if (1 == e.which) {
    //         return false;
    //     }
    // });
    $(btn).bind('contextmenu', function () {
        return false;
    });
}

function wordStatic(input, type) {

    if (!$(input).length > 0) {
        return false;
    }
    var text = $(input).val();
    text = text.replace(/\r\n/g, " ")
    text = text.replace(/\n/g, " ");

    var arr = text.split(" ");
    for (var i = 0; i < arr.length; i++) {

        if (arr[i].length < 1) {
            arr.splice(i, 1);
            i = i - 1;
        }
    }
    $(input).next().children("i").html(arr.length);
    if (type == "graph") {
        if (arr.length < 150 || arr.length > 180) {
            $(input).next().children("i").css('color', 'red')
        } else {
            $(input).next().children("i").css('color', 'green')
        }
    }
    if (type == "great") {
        if (arr.length < 250 || arr.length > 280) {
            $(input).next().children("i").css('color', 'red')
        } else {
            $(input).next().children("i").css('color', 'green')
        }
    }
}

//展开和收缩
function doggle_element(btn, parent, collap_other) {
    var hasin = $(btn).hasClass("in");
    if (collap_other) {
        $(btn).parent().parent().children('div').each(function () {
            $(this).children('.collapse').removeClass('in')
            $(this).children('.collapse').prev().children('img').addClass('xialaup');
        });
    }

    if (hasin) {
        $(btn).removeClass('in'); //隐藏
        $(btn).prev().children('img').addClass('xialaup')
    } else {
        $(btn).addClass('in');
        $(btn).prev().children('img').removeClass('xialaup')
    }
    if (parent != "") {

        $(parent).niceScroll().resize();
        $('.ResizeSection').niceScroll().resize();
    }
    //dom下是否有音频文件，加载音频文件src
    $(btn).find('source').each(function () {
        var src = $(this).data('src');
        if ($(this).attr('src') == "" || $(this).attr('src') == undefined) {
            $(this).attr('src', src);
            $(this).parent().load();
        }
    });

}

//展开和收缩
function doggle_element_part3(thisbtn, btn, parent, collap_other) {
    var hasin = $(btn).hasClass("in");
    if (collap_other) {
        $(btn).parent().parent().children('div').each(function () {
            $(this).children('.collapse').removeClass('in')
            $(this).children('.collapse').prev().children('img').addClass('xialaup');
        });
    }

    if (hasin) {
        $(btn).removeClass('in'); //隐藏
        $(btn).prev().children('img').addClass('xialaup')
    } else {
        $(btn).addClass('in');
        $(btn).prev().children('img').removeClass('xialaup')
    }
    if (parent != "") {

        $(parent).niceScroll().resize();
        $('.ResizeSection').niceScroll().resize();
    }

}

//展开和收缩
function doggle_element_part1(thisbtn, btn, parent, collap_other) {
    // var finished = $(parent).find('.recordingslist').find('audio').length;
    // if (!finished) {
    //     alert('请先完成录音,再查看答案！');
    //     return false;
    // }
    var hasin = $(btn).hasClass("in");
    if (collap_other) {
        $(btn).parent().parent().children('div').each(function () {
            $(this).children('.collapse').removeClass('in')
            $(this).children('.collapse').prev().children('img').addClass('xialaup');
        });
    }

    if (hasin) {
        $(btn).removeClass('in'); //隐藏
        $(btn).prev().children('img').addClass('xialaup')
    } else {
        $(btn).addClass('in');
        $(btn).prev().children('img').removeClass('xialaup')
    }
    if (parent != "") {

        $(parent).niceScroll().resize();
        $('.ResizeSection').niceScroll().resize();
    }

}

function alertCourse(btn, level) {

    popBuyCourse(true);

}

function alertAuth(btn, level) {

    if (level == 1) {
        //
        poplogin(true);
    } else {
        //popBuyVIP(true);
        popAuth(true);
        // layer.msg('暂未开放。。。', {icon: 4,time:800});
    }

}

Array.prototype.Exists = function (v) {
    var b = false;
    for (var i = 0; i < this.length; i++) {
        if (this[i] == v) {
            b = true;
            break;
        }
    }
    return b;
}

var initFirstContent = function () {
    try {
        var index = $('.first_category_active').attr("model_id");
        var element = $('#content' + index);
        element.css("display", "block");
    } catch (e) {
        console.log(e.toString());
    }
}

var FormatFont = function (init, ele, deep) {
    try {
        var element = ele || $('.content span');
        element.css("font-size", "14px");
        element.css("font-family", "'PingFang Regular', 'Microsoft YaHei', sans-serif");

        if (deep) {
            for (var i = 0; i < element.contents().length; i++) {
                var item = element.contents().eq(i).eq(0);
                item.css("font-size", "16px");
                item.css("font-family", "'PingFang Regular', 'Microsoft YaHei', sans-serif");
                item.css("margin", "0");
                item.children().css("font-size", "16px");
                item.children().css("font-family", "'PingFang Regular', 'Microsoft YaHei', sans-serif");
                item.children().css("font-weight", "400");
            }
        }

        if (init) {
            initFirstContent();
        }
    } catch (e) {
        console.log(e.toString());
    }
}

var AssignmentController = function () {
    var ret = this.parseParams();
    if (ret) {
        this.controlVisible();
    }
};
AssignmentController.prototype.controlVisible = function () {
    if (this.params.section) {
        var section = this.params['section'];
        var topic = this.params['topic'];
        var test = this.params['test'];
        var third = this.params['third'];
        var root = $('.' + section);
        var first_category = root.children('.first_category');

        $(first_category).find('li').each(function () {
            $(this).hide();
            if ($(this).data('model-id') == topic) {
                $(this).show().addClass('first_category_active');
            }
        });

        $(root).children('.second_category').each(function () {
            if ($(this).data('topicid') == topic) {
                $(this).show();
                $(this).find('.item-box-content').each(function () {
                    if ($(this).data('test-id') == test) {
                        $(this).show();
                        $(this).children('.collapse').addClass('in');
                        $(this).find('.third-box').each(function () {
                            if ($(this).data('third-id') == third) {
                                $(this).show();
                            } else {
                                $(this).hide();
                            }
                        });
                    } else {
                        $(this).hide();
                    }
                });
            } else {
                $(this).hide();
            }
        });

    }
};
AssignmentController.prototype.parseParams = function () {

    var searchURL = window.location.href.split('?')[1];
    if (searchURL == undefined) {
        return false;
    }
    searchURL = searchURL.split('#')[0];
    var targetPageId = searchURL.split("&");
    this.params = {};
    var newTarget = [];
    for (var i = 0; i < targetPageId.length; i++) {
        var tempArr = targetPageId[i].split('=');
        this.params[tempArr[0]] = tempArr[1];
    }
    console.log(this.params);
    return true;

};