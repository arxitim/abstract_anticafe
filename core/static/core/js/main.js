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

function openModalQR(pk) {
    event.preventDefault();

    $('#qrcode').empty();
    var qrcode = new QRCode(document.getElementById('qrcode'), {
	text: window.location.host + '/staff/' +  pk,
	colorDark : "#000000",
	colorLight : "#ffffff",
    });

    $('.overlay').fadeIn(100, function() {
        $('.qrModal')
            .css('display', 'block')
            .animate({
                opacity: 1
            }, 110);
    });
};

function deleteBooking(event, pk) {
    event.stopPropagation();
    swal({
            title: "Are you sure?",
            text: "You will delete this booking!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((willDelete) => {
            if (willDelete) {
                swal("Poof! Your booking has been deleted!", {
                    icon: "success",
                });
            }
        });
};

$('.qrModal__close, .overlay').click(function() {
    $('.qrModal').animate({
            opacity: 0.5
        }, 70,
        function() {
            $(this).css('display', 'none');
            $('.overlay').fadeOut(80);
        });
});