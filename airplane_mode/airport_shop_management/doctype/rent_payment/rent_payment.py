import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import nowdate, add_days, formatdate

class RentPayment(Document):
    pass

@frappe.whitelist()
def create_rent_payment(shop_number, amount):
    # Get the shop document
    shop = frappe.get_value("Shop", {"number": shop_number}, "name")

    if not shop:
        frappe.throw(_("Shop not found"))

    # Create the rent payment document
    rent_payment = frappe.get_doc({
        "doctype": "Rent Payment",
        "shop": shop,
        "payment_date": nowdate(),
        "payment_received": amount
    })
    rent_payment.insert()
    frappe.db.commit()
    
    return rent_payment.name

def generate_rent_receipt(rent_payment):
    return frappe.get_print("Rent Payment", rent_payment, "Rent Receipt")

@frappe.whitelist()
def send_rent_reminders():
    today = nowdate()

    tenants = frappe.get_all('Shop', fields=['tenant', 'name', 'rent_amount', 'date_of_expiry'], filters={'status': 'Occupied'})

    for tenant in tenants:
        # Check if the rent is due within the next 30 days
        if tenant.date_of_expiry and (tenant.date_of_expiry <= add_days(today, 30)):
            tenant_details = frappe.get_doc('Tenant', tenant.tenant)
            
            subject = "Rent Due Reminder"
            message = f"""
            Dear {tenant_details.tenant_name},
            
            This is a reminder that your rent for the shop {tenant.name} is due on {formatdate(tenant.date_of_expiry)}.
            
            Rent Amount: {tenant.rent_amount}
            
            Please ensure that the payment is made by the due date.
            
            Thank you.
            """

            frappe.sendmail(
                recipients=[tenant_details.email],
                subject=subject,
                message=message
            )
