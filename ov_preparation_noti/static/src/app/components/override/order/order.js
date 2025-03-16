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

        const session = await this.orm.call("pos.order", "search_read",
         [[['id','=',this.props.order.id]]],
        {fields: ['session_id']}
        );

        const session_name = session[0]['session_id'][0];
            console.log(session);
        await this.orm.call("pos.session", "change_order_stage",["",session_name]);


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