var serializeJson = function (formId) {
    var data = $("#" + formId).serializeArray();
    var result = {};
    for (var i in data) {
        var obj = data[i];
        result[obj.name] = obj.value;
    }
    if (result.id === "") result.id = 0;
    return result;
};

var showError = function (message, id) {
    if (id) {
        element = $("#" + id + "-error");
        element.html(message);
        element.show();
        $("#" + id + "-form-group").addClass("has-error");
    } else {
        error = $("#error");
        error.show();
        error.html(message);
    }
}

var hideError = function () {
    $("#error").hide();
    //$("div.help-block").html("");
    $("div[id$='-error']").html("");
    $("div[id$='-form-group']").removeClass("has-error");
}


var LODOP;

function doPrint(obj) {
    if (!LODOP) {
        LODOP = getLodop();
    }
    LODOP.PRINT_INITA(0, 0, 522, 333, "");
    LODOP.SET_PRINT_PAGESIZE(0, 560, 880);
    var left = 10;
    var height = 15;
    LODOP.SET_PRINT_STYLE("FontColor", 16711680);
    //LODOP.ADD_PRINT_RECT(62,16,459,217,0,1);
    LODOP.ADD_PRINT_TEXT(height, 30, 157, 25, "光趣商城消费明细");
    LODOP.SET_PRINT_STYLEA(2, "FontName", "隶书");
    LODOP.SET_PRINT_STYLEA(2, "FontSize", 13);
    //LODOP.SET_PRINT_STYLEA(2,"FontColor",0);
    //LODOP.SET_PRINT_STYLEA(4,"FontColor",0);
    var print = function (str, increaseBy) {
        if (!increaseBy) increaseBy = 20;
        height += increaseBy;
        LODOP.ADD_PRINT_TEXT(height, left, 431, 20, str);
    };
    print("影厅：" + obj.hall_name, 25);
    print("卡号：" + obj.member_id);
    print("姓名：" + obj.member_title);
    print("开始：" + obj.start_time);
    print("结束：" + obj.end_time);
    print("-------消费明细---------");
    print("影片: " + obj.expense + "元");
    print("-------消费明细---------");
    print("余额：" + obj.balance + "元");
    print("-------------------------");
    print("交易号:" + obj.order_id);
    print("收银员:" + obj.user_id);
    print("电  话:" + obj.telephone);
    LODOP.PREVIEW();
}









