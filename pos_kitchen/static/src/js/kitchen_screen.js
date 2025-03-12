/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from  "@odoo/owl";

 class KitchenScreen extends Component{
    static template = "pos_kitchen.kitchen_screen";

    setup(){
        if(this.props.action.context){
            console.log(this.props.action.context);
        }
    }

}

registry.category("actions").add("pos_kitchen.KitchenScreen",KitchenScreen);