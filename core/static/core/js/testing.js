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

//https://xdsoft.net/jqplugins/datetimepicker/
$(function() {
    //  A day to which you can book
    var datetime_max = new Date();
    datetime_max.setDate(datetime_max.getDate() + 31);

    var data = {
        step: 30,
        theme: "dark",
        format: 'd/m/Y H:i',
        minDate: new Date(),
    };

    $.datetimepicker.setLocale('ru');

    $("#id_dt_start").datetimepicker(Object.assign(data, {
        minTime: "17:00",
        maxDate: datetime_max,
    }));

    $("#id_dt_end").datetimepicker(Object.assign(data, {}));

    $('.dt_end').click(function() {
        var dt_start_str = $('#id_dt_start').val();
        // TODO: доделать динамическое ограничение на это поле исходя из #id_dt_start
    });
});
