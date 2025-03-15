/* @odoo-module */

import { Order } from "@pos_preparation_display/app/components/order/order";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";


patch(Order.prototype, {
    setup(){
        super.setup();
        this.orm = useService("orm");
    },
       async clickOrder() {
        console.log(this);
        console.log(this.props);
        const is_noti = await this.orm.call("pos_preparation_display.stage", "search_read",
         [[['id','=',this.props.order.stageId]]],
        {fields: ['is_noti']}
        );

        console.log(is_noti);
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