// https://xdsoft.net/jqplugins/datetimepicker/
$(function() {
    //  A day to which you can book
    var max_datetime_booking = new Date();
    max_datetime_booking.setDate(max_datetime_booking.getDate() + 31);

    // Here we must specify the minimum time for the reservation,
    // which is one hour longer than the current time, up to a round full time.
    var min_datetime_booking = new Date();
    min_datetime_booking.setHours(min_datetime_booking.getHours() + 1);
    min_datetime_booking.setMinutes(0);

    var min_datetime_str = min_datetime_booking.getFullYear() +
                           '/' + (min_datetime_booking.getMonth() + 1) +
                           '/' + min_datetime_booking.getDate() +
                           ' ' + min_datetime_booking.getHours() +
                           ':' + min_datetime_booking.getMinutes();

    var parameters = {
        theme: "dark",
        format: 'd/m/Y H:i',
        defaultDate: min_datetime_booking, // to avoid uneven minutes, like 3:37 p.m.
        defaultTime: '17:00',
        allowTimes: [
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00",
        ],
    }

    $.datetimepicker.setLocale('en');

    $("#id_dt_start").datetimepicker(Object.assign(parameters, {
        minDate: min_datetime_str,
        maxDate: max_datetime_booking
    }));

    $("#id_dt_end").datetimepicker(Object.assign(parameters, {
        minDate: min_datetime_str,
        maxDate: max_datetime_booking
    }));
});