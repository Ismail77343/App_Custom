import frappe

@frappe.whitelist(allow_guest=True)
def get_workspaces():
    # قم بكتابة الاستعلامات اللازمة للحصول على بيانات المساحات
    workspaces = frappe.get_all('Workspace', fields=['name', 'title','parent_page'])
    return workspaces
