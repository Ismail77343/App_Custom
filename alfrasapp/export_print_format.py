import frappe
import json

def export_print_format(print_format_name, file_path):
    frappe.init(site='pvcio.com')
    frappe.connect()
    print_format = frappe.get_doc('Print Format', print_format_name)
    with open(file_path, 'w') as f:
        json.dump(print_format.as_dict(), f, indent=4)
    frappe.destroy()

if __name__ == "__main__":
    print_format_name = "Alfras Pos Invoic"
    file_path = f"/home/erp13/frappe-bench/apps/alfrasapp/alfrasapp/fixtures/{print_format_name}.json"
    export_print_format(print_format_name, file_path)
