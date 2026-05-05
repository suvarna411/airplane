# Copyright (c) 2026, suvarna and contributors
# For license information, please see license.txt

# import frappe

import frappe
from frappe.website.website_generator import WebsiteGenerator

class Shop(WebsiteGenerator):
       
    def before_insert(self):
        settings = frappe.get_single("Shop Settings")

        if self.rent_amount in (None, 0):
            self.rent_amount = settings.default_rent
    def after_insert(self):
        update_shop_counts(self.airport)

    def on_update(self):
        update_shop_counts(self.airport)

    def on_trash(self):
        update_shop_counts(self.airport)
    def before_save(self):
        if not self.route:
            self.route = (f"shops/{self.name}")

def update_shop_counts(airport):
    shops = frappe.get_all(
        "Shop",
        filters={"airport": airport},
        fields=["status"]
    )

    total = len(shops)
    occupied = len([s for s in shops if s.status == "Occupied"])

    frappe.db.set_value("Airport", airport, {
        "total_shops": total,
        "occupied_shops": occupied,
        "available_shops": total - occupied
    })
def send_rent_reminders():
    settings = frappe.get_single("Shop Settings")

    if not settings.enable_rent_reminder:
        return

    shops = frappe.get_all(
        "Shop",
        filters={"status": "Occupied"},
        fields=["name", "email"]
    )

    for shop in shops:
        if shop.email:
            frappe.sendmail(
                recipients=shop.email,
                subject="Rent Due Reminder",
                message=f"Rent due for shop {shop.name}"
            )
