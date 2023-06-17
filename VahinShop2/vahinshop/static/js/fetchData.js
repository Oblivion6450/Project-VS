function fetchData(id) {
    const myInput = document.getElementById("amountCounter_"+id);
    res_request = {
        quantity: myInput.value,
        update: false,
        csrfmiddlewaretoken: getCookie('csrftoken')
    }
    $.ajax({
        type: "POST",
        // url: "/cart_add/{{product.id}}",
        url: `/cart/add/${id}/`,
        dataType: 'json',
        data: res_request,
        success: function (data) {
            console.log('data')
            window.location.href = 'cart';
        }
    });
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
} 