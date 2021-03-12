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
                                template:"<b>Cash Purchases Returns Register </b>",
                                type:"header"
                            },
                            load_receipt,
                            purchase_datatable,
                            purchase_buttons,
                        ]
                    }
                ]
            }
        ]
    });

    // logic
    $$("load_receipt").focus();

});
