/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from  "@odoo/owl";

 class KitchenScreen extends Component{
    static template = "pos_kitchen.kitchen_screen";

}

registry.category("actions").add("pos_kitchen.KitchenScreen",KitchenScreen);