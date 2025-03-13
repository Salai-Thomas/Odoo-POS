/* @odoo-module */

import { Order } from "@pos_preparation_display/app/components/order/order";
import { patch } from "@web/core/utils/patch";

patch(Order.prototype, {
    setup(){
        super.setup();
    },
       async clickOrder() {
        console.log(this);
        console.log(this.props);
        if (this.actionInProgress) {
            return;
        }
        try {
            this.actionInProgress = true;
            const order = this.props.order;
            if (order.stageId === this.preparationDisplay.lastStage.id) {
                return;
            } else {
                await this.preparationDisplay.sendStrickedLineToNextStage(this.props.order);
            }
        } catch (error) {
            console.warn(error);
        } finally {
            this.actionInProgress = false;
        }
    }

});