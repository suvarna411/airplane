// Copyright (c) 2026, suvarna and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Airline", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            frm.add_custom_button('Open Website', function() {
                window.open(frm.doc.website);
            });
        }
    }
});
