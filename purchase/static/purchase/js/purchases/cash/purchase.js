webix.ready(function(){
    // layout
    webix.ui({
        // type:"wide",
        rows:[
           toolbar,
            {
                cols:[
                    side,
                    {
                        type:"space",
                        rows:[
                            {
                                template:"<b>Cash Purchases Register </b>",
                                type:"header"
                            },
                            get_product,
                            purchase_datatable,
                            purchase_buttons,
                        ]
                    }
                ]
            }
        ]
    });

    // windows
    webix.ui(get_product_window);
    webix.ui(get_supplier_window);
    webix.ui(product_window);

    // logic
    var product_list = $$("get_product").getPopup().getList();
    product_list.clearAll();
    product_list.load("/inventory/apiv1/helpers/getproductidface");
    $$("get_product").focus();
    var supplier_list = $$("get_supplier").getPopup().getList();
    supplier_list.clearAll();
    supplier_list.load("/supplier/apiv1/helpers/getsupplieridface");
    var category_list = $$("product_form").elements.category.getPopup().getList();
    category_list.clearAll();
    category_list.load("/inventory/apiv1/helpers/getcategoryidface");
    var payment_system_list = $$("get_payment_system").getPopup().getList();
    payment_system_list.clearAll();
    payment_system_list.load("/cash/apiv1/helpers/systems");
    $$("get_product").focus();
});
