webix.ready(function(){
    // layout
    var space = {
        type:"space",
        view:"accordion",
        multi:true,
        cols:[
            {
                header:'Currently Loged In User',
                body:{
                    padding:20,
                    cols:[
                        {
                            view:"property",
                            width:300,
                            url:"/access/userdata",
                            elements:[
                               { label:"User Information", type:"label"},
                               { label:"Username",id:"username"},
                               { label:"First Name", id:"first_name"},
                               { label:"Last Name",id:"last_name"},
                               { label:"email",id:"email"}
                            ]
                        }
                    ]
                },
            },
            {
                header:'Help',
                body:'Use Click on the menu to see the parts of the application you have access to.',
            },
            {
                header:'About Us',
                body:'We specializes in creating customized softwares to meet your business and personal needs, kindly contact us for more information.',
            }
        ]
    };

    webix.ui({
        // type:"wide",
        rows:[
            toolbar,
            {
                cols:[
                    side,
                    space
                ]
            }
        ]
    });

    // windows

});
