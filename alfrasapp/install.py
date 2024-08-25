import frappe

def remove_onboarding():
    # التأكد من أن المستخدم قد تم تسجيل دخوله
    # if frappe.session.user != "Guest":
        # حذف الإرشادات الخاصة بالتطبيقات المثبتة
    frappe.db.sql("""DELETE FROM `tabOnboarding Step` """)

def after_install_tasks():
    # استدعاء الدوال التي ترغب في تنفيذها بعد التثبيت
    disable_update_popup()
    print("Done disable_show_update_popup ")
    remove_onboarding()
    # يمكنك إضافة دوال أخرى هنا

def disable_update_popup():
    # تعطيل ظهور رسالة التحديث
    frappe.db.set_value("System Settings", "System Settings", "disable_system_update_notification", 1)
    frappe.clear_cache()
