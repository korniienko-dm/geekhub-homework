$(document).ready(function () {
    $(".updateQuantityBtn").click(function () {
        var form = $(this).closest(".cart_form");

        if (form[0].checkValidity()) {
            var product_id = form.data("id");
            var quantity = form.find(".numberInput").val();
            var price = form.data("price");

            $.ajax({
                type: "POST",
                url: "/send_quantity_products/",
                data: {
                    csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                    product_id: product_id,
                    quantity: quantity,
                    price: price
                },
                success: function (response) {
                    $.get("/cart/", function (data) {
                        $.get("/get_product_price/" + product_id, function (data) {
                            $("#price_product_" + product_id).text("$ " + data.price);
                            console.log("Change price RUN - Success - Price - " + data.price)
                        });
                    });    
                },
                error: function () {
                    alert("Error processing the request.");
                }
            });
        } else {
            alert("Form is invalid");
        }
    });
});
