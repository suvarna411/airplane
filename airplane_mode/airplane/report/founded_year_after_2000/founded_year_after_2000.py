import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Airline", "fieldname": "name", "fieldtype": "Data", "width": 200},
        {"label": "Founding Year", "fieldname": "founding_year", "fieldtype": "Int", "width": 120},
        {"label": "Headquarters", "fieldname": "headquarters", "fieldtype": "Data", "width": 200},
        {"label": "Website", "fieldname": "website", "fieldtype": "Data", "width": 200},
    ]

def get_data(filters):
    conditions = ""
    
    if filters.get("founding_year"):
        conditions += " AND founding_year >= %(founding_year)s"

    return frappe.db.sql(f"""
        SELECT
            name,
            founding_year,
            headquarters,
            website
        FROM `tabAirline`
        WHERE 1=1 {conditions}
    """, filters, as_dict=True)
# For license information, please see license.txt

# import frappe



