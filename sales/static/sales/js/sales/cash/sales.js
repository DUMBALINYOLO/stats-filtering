webix.ready(function () {
    // layout
    webix.ui({
        // type:"wide",
        rows: [
            toolbar,
            {
                cols: [
                    side,
                    {
                        type: 'space',
                        rows: [
                            {
                                template: "<b>Cash Point of Sales [ Instant Payment ]</b>",
                                type: "header"
                            },
                            {
                                view: "tabview",
                                cells: [{
                                    header: "Sell Here",
                                    body: {
                                        // paddingX:10,
                                        type: "space",
                                        rows: [

                                            get_product,
                                            sales_datatable,
                                            sales_buttons,
                                        ]
                                    }
                                },
                                cash_sales
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
    });

    // windows
    webix.ui(get_product_window);
    webix.ui(customer_window);

    // logic
    var product_list = $$("get_product").getPopup().getList();
    product_list.clearAll();
    product_list.load("/inventory/apiv1/helpers/getproductidface");
    $$("get_product").focus();
    var payment_system_list = $$("get_payment_system").getPopup().getList();
    payment_system_list.clearAll();
    payment_system_list.load("/cash/apiv1/helpers/systems");

});
