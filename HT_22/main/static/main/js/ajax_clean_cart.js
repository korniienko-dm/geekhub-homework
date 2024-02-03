$(document).ready(function () {
    $("#a_btn").click(function (event) {
        event.preventDefault();
        $.ajax({
            type: "GET",
            url: "/cart",
            success: function (response) {
                $.get("/clean_cart/", function () {
                    console.log("/clean_cart/ - RUN")
                    $.get("/get_cart_count", function (data) {
                        $(".count_product").text(data.count);
                        console.log("/get_cart_count - RUN; Value -" + data.count)
                    });
                });

                $("#cart_wrapper").append('<div class="empty_product_list">' +
                '<p><strong>You don\'t have any added products to <b>cart</b>.</strong></p>' +
                '<p>Please visit the page: <a href="/show_all_products">"Products"</a> and add the products to your cart.</p>' +
                '</div>');

                $(".table").empty(); 
                $(".clean_cart").empty(); 
            },
            error: function () {
                alert("Error processing the request.");
            }
        });
    
    });
});

