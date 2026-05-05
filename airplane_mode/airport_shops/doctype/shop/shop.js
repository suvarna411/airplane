// Copyright (c) 2026, suvarna and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Shop", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Shop', {
    setup: function(frm) {
        frm.set_query('shop_type', function() {
            return {
                filters: {
                    enabled: 1
                }
            };
        });
    }
});
