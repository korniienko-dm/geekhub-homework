$(document).ready(function () {
    $(".td_cart").click(function (event) {
        event.preventDefault();
        var product_id = $(this).data("product-id");
        
        $.ajax({
            type: "GET",
            url: "/swap_product_in_cart",
            data: { product_id: product_id },
            success: function (response) {
                var imgElement = $(event.target);
                if (imgElement.attr("src").includes("inside_cart")) {
                    imgElement.attr("src", "/static/cart/img/del_from_cart.png");
                } else {
                    imgElement.attr("src", "/static/cart/img/inside_cart.png");
                }
                
                $.get("/get_cart_count", function (data) {
                    $(".count_product").text(data.count);
                });
            },
            error: function () {
                alert("Error processing the request.");
            }
        });
    });
});
