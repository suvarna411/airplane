# Copyright (c) 2026, suvarna and contributors
# For license information, please see license.txt

# import frappe


import frappe
from frappe.model.document import Document
from frappe import _


class TravelRequest1(Document):

    def validate(self):
        self.validate_dates()
        self.validate_expenses()
        self.calculate_total()
        self.prevent_duplicate_expenses()

    def validate_dates(self):
        if self.from_date and self.to_date:
            if self.from_date > self.to_date:
                frappe.throw(_("From Date cannot be after To Date"))

    def validate_expenses(self):
        if not self.custom_expenses:
            frappe.throw(_("At least one expense is required"))

    def calculate_total(self):
        total = 0
        for row in self.custom_expenses:
            total += row.amount or 0
        self.total_estimated_amount = total

    def prevent_duplicate_expenses(self):
        seen = []
        for row in self.custom_expenses:
            if row.expense_type in seen:
                frappe.throw(_("Duplicate expense type not allowed"))
            seen.append(row.expense_type)
