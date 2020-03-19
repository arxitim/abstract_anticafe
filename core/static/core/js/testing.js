function redirectToHome() {
  window.location.replace('/');
}

function bookingNow(table_id) {
    /**
     * ajax-request feature
     * to process booking operation
     */
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/api/booking_now/" + table_id,
        dataType: "json",
        data: {
            csrfmiddlewaretoken: document.cookie.slice(10),

        },
        success: function(data) {
            if (data.status) {
                alert("Успешно заказан столик")
                setTimeout(redirectToHome, 2000)
            } else {
                alert("Упс, вы накосячили")
            }
        }
    });
};

$('.apireq').click(function() {
    /**
     * ajax-request feature
     * to find out more about your account
     */
    $.ajax({
        url: "http://127.0.0.1:8000/api/account_info/",
        dataType: "json",
        success: function(data) {
            $('#id').text(data.id);
            $('#email').text(data.email);
            $('#username').text(data.username);
            $('#last_login').text(data.last_login);
        }
    });
});