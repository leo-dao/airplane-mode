// Copyright (c) 2024, Leo Dao and contributors
// For license information, please see license.txt

frappe.ui.form.on('Airplane Ticket', {
    refresh: function(frm) {
        // Add custom button
        frm.add_custom_button(__('Set Seat Number'), function() {
            // Show dialog to get seat number
            let d = new frappe.ui.Dialog({
                title: __('Enter Seat Number'),
                fields: [
                    {
                        label: __('Seat Number'),
                        fieldname: 'seat_number',
                        fieldtype: 'Data'
                    }
                ],
                primary_action_label: __('Set'),
                primary_action(values) {
                    // Set the Seat field value in the form
                    frm.set_value('seat', values.seat_number);
                    d.hide();
                }
            });
            d.show();
        });
    }
});
