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
    delAdm = $("#delAdm")
    if (obj == "5"){
        adm.show()
        delAdm.hide()
        delAdm.style.display = "none"
    }
    if(obj == "6"){
        adm.hide()
        delAdm.show()
        delAdm.style.display = "block"
    }
}