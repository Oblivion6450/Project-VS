

$.ajax({
            type: "GET",
            url: '{% url "api_cart" %}',
            dataType: 'json',
            data: res_request,
            success: function (data) {
                closeModal()
                let cart_sum = document.getElementById('cart')
                cart_sum.textContent = data['cart_sum']
                let cart_count = document.getElementById('count')
                cart_count.textContent = data['cart_count']
            }
        });
    }