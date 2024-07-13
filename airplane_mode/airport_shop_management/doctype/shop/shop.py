# Copyright (c) 2024, Leo Dao and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document
import random

class Shop(Document):

    def before_insert(self):
        if not self.number:
            self.number = self.generate_unique_random_number()

        if not self.rent_amount:
            self.rent_amount = frappe.get_value('Shop Settings', None, 'default_rent_amount')

            
    def generate_unique_random_number(self):
        while True:
            random_number = str(random.randint(100000, 999999))
            if not frappe.db.exists("Shop", {"number": random_number}):
                return random_number