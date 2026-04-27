import frappe

def create_travel_log(doc, method):
    log = frappe.get_doc({
        "doctype": "Travel Approval Log",
        "travel_request_id": doc.name,
        "employee": doc.employee,
        "department": doc.department,
        "total_estimated_amount": doc.total_estimated_amount,
        "submitted_on": frappe.utils.now()
    })
    log.insert(ignore_permissions=True)
