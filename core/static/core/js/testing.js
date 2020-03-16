function bookingNowTest(table_id) {
    alert(document.cookie.slice(10))
}

function bookingNow(table_id) {
    $.ajax({
             type: "POST",
             url : "http://127.0.0.1:8000/api/booking_now/" + table_id,
             dataType: "json",
             data: {csrfmiddlewaretoken: document.cookie.slice(10)},
             success : function (data) {
                      alert("Успешно заказан столик");
                    }
                 });
             };

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