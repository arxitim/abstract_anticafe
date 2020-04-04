function redirectToHome() {
    window.location.replace('/');
}

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
