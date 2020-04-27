function redirectToHome() {
    window.location.replace("/");
}

$(".apireq").click(function() {
    /**
     * ajax-request feature
     * to find out more about your account
     */
    $.ajax({
        url: "http://192.168.0.14:8000/api/account_info/",
        dataType: "json",
        success: function(data) {
            $("#id").text(data.id);
            $("#email").text(data.email);
            $("#username").text(data.username);
            $("#last_login").text(data.last_login);
        }
    });
});

function openModalQR(pk) {
    event.preventDefault();

    $("#qrcode").empty();
    var qrcode = new QRCode(document.getElementById("qrcode"), {
	text: window.location.host + "/staff/" +  pk,
	colorDark : "#000000",
	colorLight : "#ffffff",
    });

    $(".overlay").fadeIn(100, function() {
        $(".qrModal")
            .css("display", "block")
            .animate({
                opacity: 1
            }, 110);
    });
};

function successBookingDelete(pk) {
    $("#" + pk).remove();
    swal("Poof! Your booking has been deleted!", {
        icon: "success",
        button: {
            className: "btn-secondary swal-button btn-md"
        },
    });
};

function failedBookingDelete(pk) {
    swal("Your booking has not been deleted!", {
        icon: "error",
        button: {
            className: "btn-secondary swal-button btn-md"
        },
    });
};

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        var cookies = document.cookie.split(";");
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function deleteBooking(event, pk) {
    event.stopPropagation();
    var deleteModal = swal({
        title: "Are you sure?",
        text: "You will delete this booking!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    })

    //  Crutch to remove a fucking line the size of a pixel when closing the modal
    $(".swal-overlay").removeAttr("tabindex");
    //

    deleteModal.then((willDelete) => {
        if (willDelete) {
            $.ajax({
                type: "DELETE",
                url: "http://127.0.0.1:8000/api/delete_booking/" + pk,
                dataType: "json",
                beforeSend: function (xhr) {
                    xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
                },
                success: function(data) {
                    if (data.status) {
                        successBookingDelete(pk);
                    } else {
                        failedBookingDelete();
                    }
                },
                error: function() {
                    failedBookingDelete();
                }
            })
        }
    });
};

$(".qrModal__close, .overlay").click(function() {
    $(".qrModal").animate({
            opacity: 0.5
        }, 70,
        function() {
            $(this).css("display", "none");
            $(".overlay").fadeOut(80);
        });
});