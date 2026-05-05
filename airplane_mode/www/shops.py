import frappe

def get_context(context):
    context.shops = frappe.get_all(
        "Shop",
        fields=[ "shop_name", "route"]
    )
