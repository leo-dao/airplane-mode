frappe.ui.form.on('Shop', {
    refresh: function(frm) {
        frm.add_custom_button(__('Record Rent Payment'), function() {
            frappe.prompt([
                {'fieldname': 'amount', 'fieldtype': 'Currency', 'label': 'Amount', 'reqd': 1}
            ],
            function(values){
                frappe.call({
                    method: 'airplane_mode.airport_shop_management.doctype.rent_payment.rent_payment.create_rent_payment',
                    args: {
                        shop_number: frm.doc.number,
                        amount: values.amount
                    },
                    callback: function(response) {
                        let rent_payment = response.message;
                        frappe.show_alert(__('Rent Payment recorded successfully.'));
                        frappe.set_route('Form', 'Rent Payment', rent_payment.name);
                    }
                });
            },
            __('Record Rent Payment'),
            __('Record')
            );
        });
    }
});
