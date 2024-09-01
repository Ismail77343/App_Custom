# import os
# import frappe

# # def remove_onboarding():
# #     # التأكد من أن المستخدم قد تم تسجيل دخوله
# #     # if frappe.session.user != "Guest":
# #         # حذف الإرشادات الخاصة بالتطبيقات المثبتة
# #     frappe.db.sql("""DELETE FROM `tabOnboarding Step` """)

# # def after_install():
# #     import shutil
# #     import os
# #     print("Full Path:", os.path.abspath("apps/alfrasapp/alfrasapp/templates/includes/header.html"))

# #     shutil.copy("/home/erp15/frappe-trade/apps/alfrasapp/alfrasapp/templates/includes/header.html", "/home/erp15/frappe-trade/apps/frappe/frappe/public/js/frappe/ui/toolbar/header.html")
# #     shutil.copy("/home/erp15/frappe-trade/apps/alfrasapp/alfrasapp/templates/includes/workspace.html", "/home/erp15/frappe-trade/apps/frappe/frappe/public/js/frappe/ui/toolbar/workspace.html")


# #     # # نسخ ملف header المخصص
# #     # shutil.copy("apps/alfrasapp/alfrasapp/templates/includes/header.html", "apps/frappe/frappe/public/js/frappe/ui/toolbar/header.html")
    
# #     # # نسخ ملف workspace المخصص
# #     # shutil.copy("apps/alfrasapp/alfrasapp/templates/includes/workspace.html", "apps/frappe/public/js/frappe/ui/toolbar/workspace.html")
    

# # def after_install_tasks():
# #     # استدعاء الدوال التي ترغب في تنفيذها بعد التثبيت







