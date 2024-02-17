$(document).ready(function () {
    $(".td_cart").click(function (event) {
        event.preventDefault();
        var clickedElement = $(this);
        var product_id = $(this).data("product-id");
        
        $.ajax({
            type: "GET",
            url: "/swap_product_in_cart",
            data: { product_id: product_id },
            success: function (response) {
                console.log('Delete product - success')
                
                $.get("/get_cart_count", function (data) {
                    $(".count_product").text(data.count);
                });

                var rowToRemove = clickedElement.closest('tr');
                rowToRemove.remove();
            },
            error: function () {
                alert("Error processing the request.");
            }
        });
    });
});