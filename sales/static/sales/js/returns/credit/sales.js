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
                                template:"<b>Credit Sales Returns Register</b>",
                                type:"header"
                            },
                            load_invoice,
                            sales_datatable,
                            sales_buttons,
                        ]
                    }
                ]
            }
        ]
    });

    // logic
    $$("load_invoice").focus();

});
