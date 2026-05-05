// Copyright (c) 2026, suvarna and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airplane Ticket", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {

       
        frm.clear_custom_buttons();

        frm.add_custom_button('Assign Seat', function() {

            let d = new frappe.ui.Dialog({
                title: 'Enter Seat Number',
                fields: [
                    {
                        label: 'Seat',
                        fieldname: 'seat',
                        fieldtype: 'Data',
                        reqd: 1
                    }
                ],
                primary_action(values) {

                    console.log("Seat Entered:", values.seat); // debug

                    frm.set_value('seat', values.seat);
                    frm.refresh_field('seat');

                    d.hide();
                }
            });

            d.show();
        });
    }
});      
