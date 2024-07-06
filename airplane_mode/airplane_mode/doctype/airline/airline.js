// Copyright (c) 2024, Leo Dao and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airline', {
    refresh: function(frm) {
        if (frm.doc.website) {
            frm.add_custom_button('Visit Website', () => {
                window.open(frm.doc.website, '_blank');
            });
        }
    }
});