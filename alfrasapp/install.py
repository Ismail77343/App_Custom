import os
import frappe

def remove_onboarding():
    # التأكد من أن المستخدم قد تم تسجيل دخوله
    # if frappe.session.user != "Guest":
        # حذف الإرشادات الخاصة بالتطبيقات المثبتة
    frappe.db.sql("""DELETE FROM `tabOnboarding Step` """)

def after_install():
    import shutil
    import os
    print("Full Path:", os.path.abspath("apps/alfrasapp/alfrasapp/templates/includes/header.html"))

    shutil.copy("/home/erp15/frappe-trade/apps/alfrasapp/alfrasapp/templates/includes/header.html", "/home/erp15/frappe-trade/apps/frappe/frappe/public/js/frappe/ui/toolbar/header.html")
    shutil.copy("/home/erp15/frappe-trade/apps/alfrasapp/alfrasapp/templates/includes/workspace.html", "/home/erp15/frappe-trade/apps/frappe/frappe/public/js/frappe/ui/toolbar/workspace.html")


    # # نسخ ملف header المخصص
    # shutil.copy("apps/alfrasapp/alfrasapp/templates/includes/header.html", "apps/frappe/frappe/public/js/frappe/ui/toolbar/header.html")
    
    # # نسخ ملف workspace المخصص
    # shutil.copy("apps/alfrasapp/alfrasapp/templates/includes/workspace.html", "apps/frappe/public/js/frappe/ui/toolbar/workspace.html")
    

def after_install_tasks():
    # استدعاء الدوال التي ترغب في تنفيذها بعد التثبيت
    disable_update_popup()
    print("Done disable_show_update_popup ")
    remove_onboarding()
    # يمكنك إضافة دوال أخرى هنا
    # after_install()
    remove_erpnext_links()
    print("Done Remove Links ")

    remove_help_dropdown()
    print("Done Remove DropDown Help ")

    # print("Letter Head Defult Added ")

def disable_update_popup():
    # تعطيل ظهور رسالة التحديث
    frappe.db.set_value("System Settings", "System Settings", "disable_system_update_notification", 1)
    frappe.db.set_value("System Settings", "System Settings", "enable_onboarding", 0)
    frappe.clear_cache()






def remove_erpnext_links():
    # تحديد مسارات القوالب والملفات في تطبيق ERPNext
    paths_to_scan = [
        frappe.get_app_path('frappe', 'templates'),
        frappe.get_app_path('erpnext', 'templates'),
        frappe.get_app_path('alfrasapp', 'templates'),  # إذا كان لديك قوالب مخصصة
        # أضف مسارات أخرى إذا لزم الأمر
    ]
    
    # الروابط التي تشير إلى موقع ERPNext
    patterns_to_remove = [
        'erpnext.com',
        'https://erpalfras.ddns.net',
        'http://erpnext.com',
        'https://erpalfras.ddns.net/',
        'docs.erpnext.com',
    ]
    
    # فحص جميع الملفات في المسارات المحددة
    for path in paths_to_scan:
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name.endswith(('.html', '.js', '.py')):  # افحص ملفات HTML و JS و Python
                    file_path = os.path.join(root, file_name)
                    with open(file_path, 'r+') as file:
                        content = file.read()
                        new_content = content
                        for pattern in patterns_to_remove:
                            new_content = new_content.replace(pattern, '# Link Removed')
                        if content != new_content:
                            file.seek(0)
                            file.write(new_content)
                            file.truncate()

    frappe.msgprint("ERPNext links have been removed successfully.")



def remove_help_dropdown():
    # البحث عن جميع عناصر Navbar التي تحتوي على "Help" في التسمية
    help_items = frappe.get_all('Navbar Item', filters={'item_label': ['like', '%Help%']})

    for item in help_items:
        # حذف العنصر الذي يحتوي على "Help"
        frappe.delete_doc('Navbar Item', item.name)
    
    frappe.msgprint("All 'Help' dropdowns and related items have been removed from the Navbar.")





