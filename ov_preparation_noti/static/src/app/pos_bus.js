/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { PosBus } from "@point_of_sale/app/bus/pos_bus_service";

patch(PosBus.prototype, {
 dispatch(message) {
        super.dispatch(...arguments);

        if(message.type == "kitchen"){
            console.log("ok")
        }
    },

  });