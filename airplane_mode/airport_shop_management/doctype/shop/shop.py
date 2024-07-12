# Copyright (c) 2024, Leo Dao and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random

class Shop(Document):
    pass


def before_insert(self):
    if not self.number:
        self.number = self.generate_unique_random_number()

def after_insert(doc, method):
    Shop.update_airport_shop_count(doc.airport)

def on_trash(doc, method):
    Shop.update_airport_shop_count(doc.airport)

def on_update(doc, method):
    Shop.update_airport_shop_count(doc.airport)

def update_airport_shop_count(airport_name):
    shop_count = frappe.db.count('Shop', {'airport': airport_name})
    frappe.db.set_value('Airport', airport_name, 'shop_count', shop_count)
    frappe.db.commit()
        
def generate_unique_random_number(self):
    while True:
        random_number = str(random.randint(100000, 999999))
        if not frappe.db.exists("Shop", {"number": random_number}):
            return random_number