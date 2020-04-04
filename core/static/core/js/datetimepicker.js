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

    var parameters = {
        theme: "dark",
        format: 'd/m/Y H:i',
        defaultDate: min_datetime_booking, // to avoid uneven minutes, like 3:37 p.m.
        allowTimes: [ // TODO: deduce into a separate variable
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00",
        ],
    }

    $.datetimepicker.setLocale('ru');

    $("#id_dt_start").datetimepicker(Object.assign(parameters, {
        maxDate: max_datetime_booking,
        minDate: min_datetime_booking,
    }));

    $('.dt_end').click(function() {
        var raw_datetime_start_booking = $('#id_dt_start').val().split(" ");
        var raw_date = raw_datetime_start_booking[0].split("/");
        var raw_time = raw_datetime_start_booking[1].split(":");

        var datetime_start_booking = new Date(year = raw_date[2], month = raw_date[1], date = raw_date[0],
                                              hours = raw_time[0], minutes = raw_time[1]);

        var min_datetime_end_booking = new Date(datetime_start_booking);
        min_datetime_end_booking.setMonth(min_datetime_end_booking.getMonth() - 1); // the starting point is zero
        min_datetime_end_booking.setHours(min_datetime_end_booking.getHours() + 1);

        var max_datetime_end_booking = new Date(min_datetime_end_booking);
        max_datetime_end_booking.setHours(max_datetime_end_booking.getHours() + 3);

        $("#id_dt_end").datetimepicker(Object.assign(parameters, {
            minDate: min_datetime_end_booking,
            maxDate: max_datetime_end_booking,
        }));
    });
});