function bookingNow(table_id) {
    alert("Вы пытаетесь забронировать стол #" + table_id);
}

$('.apireq').click( function() {
    $.ajax({
             url : "http://127.0.0.1:8000/api/account_info/",
             dataType: "json",
             success : function (data) {
                      $('#id').text( data.id);
                      $('#email').text( data.email);
                      $('#username').text( data.username);
                      $('#last_login').text( data.last_login);
                    }
                 });
             });