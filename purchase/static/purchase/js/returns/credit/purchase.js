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
                                template:"<b>Credit Purchases Returns Register </b>",
                                type:"header"
                            },
                            load_invoice,
                            purchase_datatable,
                            purchase_buttons,
                        ]
                    }
                ]
            }
        ]
    });

    // logic
    $$("load_invoice").focus();

});
