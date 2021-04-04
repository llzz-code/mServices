function del(obj) {
    $.ajax({
        type: 'DELETE',
        url: '/admin/index',
        data: {id: obj, _method: 'delete'},
        success: function (data) {
            location.reload()
        },
        error: function (data) {
            alert(2);
        }
    })
}
function ret(obj) {
    $.ajax({
        type: 'PUT',
        url: '/admin/index',
        data: {id: obj, _method: 'put'},
        success: function (data) {
            location.reload()
        },
        error: function (data) {
            alert(2);
        }
    })
}
function show(obj) {
    adm = $("#adm");
    delAdm = $("#delAdm");
    add = $("#add");
    if (obj == "5"){
        adm.show();
        delAdm.hide();
        add.hide();
        delAdm.style.display = "none";
        add.style.display = "none";
    }
    if(obj == "6"){
        adm.hide();
        delAdm.show();
        add.hide();
        delAdm.style.display = "block";
        add.style.display = "none";
    }
    if(obj == "7"){
        adm.hide();
        delAdm.hide();
        add.show();
        delAdm.style.display = "none";
        add.style.display = "block";
    }
}
function register() {
    let login_id = $("#login_id").val();
    let name = $("#name").val();
    let pwd = $("#pwd").val();

    if(login_id == "" || name == "" || pwd == ""){
        $("#error").text("请填写信息")
    }else{
        let data = {
            'login_id': login_id,
            'pwd': pwd,
            'name': name
        };
        $.ajax({
        type: 'POST',
        url: '/admin/index',
        data: data,
        success: function (res) {
            location.reload()
            console.log(res.code)
        },
        error: function (res) {
            alert(2);
        }
    })
    }
}