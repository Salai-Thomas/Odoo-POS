/** @odoo-module */
import { patch } from "@web/core/utils/patch";
import { ActionpadWidget } from "@point_of_sale/app/screens/product_screen/action_pad/action_pad";
import { useService } from "@web/core/utils/hooks";

patch(ActionpadWidget.prototype,{
    setup(){
        super.setup();
        this.orm = useService("orm");
    },
    async submitOrder() {
        const order_name= this.pos.selectedOrder.name;
        await this.orm.call("pos.order","check_order_status",["",order_name]);

        if (!this.clicked) {
            this.clicked = true;
            try {
                await this.pos.sendOrderInPreparationUpdateLastChange(this.currentOrder);
            } finally {
                this.clicked = false;
            }
        }
    },
});