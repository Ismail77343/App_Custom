import frappe
# import speech_recognition as sr
# import pyaudio
import frappe.desk.search
from frappe import whitelist
from frappe.desk.search import search_link
import json
import os
import json
import openai


@whitelist(allow_guest=True)
def start_audio_recording():
    # بدء تسجيل الصوت
    audio = pyaudio.PyAudio()
    stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    frames = []

    # التسجيل لمدة 5 ثوانٍ (يمكن تعديلها حسب الحاجة)
    for i in range(0, int(44100 / 1024 * 5)):
        data = stream.read(1024)
        frames.append(data)

    # إيقاف التسجيل
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # تحويل الصوت المسجل إلى نص
    recognizer = sr.Recognizer()
    audio_data = sr.AudioData(b''.join(frames), 44100, 2)


    try:
        frappe.msgprint("hello")
        text = recognizer.recognize_google(audio_data)
        frappe.msgprint(text)  # عرض النص في رسالة
    except sr.UnknownValueError:
        frappe.msgprint("Could not understand audio")
    except sr.RequestError as e:
        frappe.msgprint("Could not request results; {0}".format(e))

@frappe.whitelist()
def Speak(text):
    text=text.lower()
    # # استخدام دالة البحث المدمجة في ERPNext للبحث عن الكلمة الرئيسية
    results = frappe.get_all("DocType", filters={'name': ['like', '%' + text + '%']})
    
    if results:
        text=text.replace(" ","-")
        # إذا تم العثور على نتائج، فافتح أول نتيجة
        doctype_name = results[0].name
        frappe.route_options = {'name': doctype_name}
        frappe.local.response["location"] = f"/app/{doctype_name}"
        doc = frappe.get_doc("DocType", doctype_name)
        frappe.set_route('Form', doc.doctype, interface_name)

        return f"/app/{text}"
    else:
        frappe.msgprint("لم يتم العثور على أي نتائج")
        return "لم يتم العثور على أي نتائج"
    # frappe.msgprint(text)
















# وظيفة لتحليل النص باستخدام OpenAI
def get_openai_response_search(prompt):
    with open('common_site_config.json') as config_file:
        config = json.load(config_file)
    openai.api_key = config['openai_api_key']

    # تحويل القائمة إلى سلسلة نصية
    interface_links_str = json.dumps(get_interface_links())

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are an AI assistant. Analyze the text and identify the ERPNext interface. Just return the URL or '0'. Here are the Data Interfaces: {interface_links_str}"},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

# دالة لجلب الروابط وأسماء الواجهات باللغتين
def get_interface_links():
    # البحث عن كل الـ DocTypes الموجودة في النظام
    doctypes = frappe.get_all("DocType", filters={"istable": 0}, fields=["name", "module", "description"])
    workspaces = frappe.get_all("Workspace", fields=["name", "module", "label"])
    reports = frappe.get_all("Report", filters={"disabled": 0}, fields=["name", "report_type", "module"])
    pages = frappe.get_all("Page", fields=["name", "module", "title"])


    interface_links = []
    for doctype in doctypes:
        doctype_name = doctype["name"]
        # إنشاء الرابط بناءً على اسم الـ DocType
        doctype_link = f"/app/{doctype_name.lower().replace(' ', '-')}"
        
        # إضافة الإدخال للمصفوفة باللغة العربية والإنجليزية
        interface_links.append({
            "Type": "doctype",
            "english_name": doctype_name,
            "arabic_name": frappe._(doctype_name),  # تستخدم Frappe للترجمة التلقائية
            "link": doctype_link
        })

    # إضافة روابط Pages
    for page in pages:
        page_name = page["name"]
        page_link = f"/app/{page_name.lower().replace(' ', '-')}"
        
        interface_links.append({
            "Type": "page",
            "english_name": page_name,
            "arabic_name": frappe._(page_name),  # تستخدم Frappe للترجمة التلقائية
            "link": page_link
        })
    
    # إضافة روابط workspaces
    for workspace in workspaces:
        page_name = workspace["name"]
        page_link = f"/app/{page_name.lower().replace(' ', '-')}"
        
        interface_links.append({
            "Type": "Workspace",
            "english_name": page_name,
            "arabic_name": frappe._(page_name),  # تستخدم Frappe للترجمة التلقائية
            "link": page_link
        })

    # إضافة روابط Report
    for Report in reports:
        page_name = Report["name"]
        page_link = f"/app/query-report/{page_name.lower()}"
        
        interface_links.append({
            "Type": "Report",
            "english_name": page_name,
            "arabic_name": frappe._(page_name),  # تستخدم Frappe للترجمة التلقائية
            "link": page_link
        })



    
    with open("filename.json", 'w') as file:
        json.dump(interface_links, file, indent=4)

    return interface_links

# دالة لتحليل النص وإرجاع رابط الواجهة المناسب
@frappe.whitelist()
def analyze_and_get_link(text):
    # interface_links = get_interface_links()
    
    # تحليل النص باستخدام OpenAI
    analyzed_text = get_openai_response_search(text)
    
    # print(analyzed_text)
    
    # if analyzed_text != 0:
    #     return {
    #             "redirect": analyzed_text,
    #             "Error": "true",
    #             "msg": "تم العثور على الواجهة وسيتم فتحها.",
    #             "lang": frappe.local.lang
    #         }
    # else:
    #    msg = get_openai_response2()
    #    return {
    #         "Error": "false",
    #         "msg": msg,
    #         "lang": frappe.local.lang
    #     } 
        
    # البحث عن الرابط المناسب بناءً على النص المستخرج
    for interface in interface_links:
        if interface["english_name"] in analyzed_text or interface["arabic_name"] in analyzed_text:
            return {
                "redirect": interface["link"],
                "Error": "true",
                "msg": "تم العثور على الواجهة وسيتم فتحها.",
                "lang": frappe.local.lang
            }

    # إذا لم يتم العثور على الواجهة المناسبة
    return {
        "Error": "false",
        "msg": "لم يتم العثور على واجهة مناسبة للنص المدخل.",
        "lang": frappe.local.lang
    }

























# قم بتخزين المحادثة السابقة في هذه القائمة
conversation_history = [
    {"role": "system", "content": "You are an AI assistant in the ERPALFRAS system. Your name is Sarah. The ERPALFRAS system is the same as the ERPNEXT system, but never say ERPNEXT and replace it with ERPALFRAS in your output. If anyone asks for your name, tell them your name is Sarah."}
]

def get_openai_response2(prompt):
    with open('common_site_config.json') as config_file:
        config = json.load(config_file)
    openai.api_key = config['openai_api_key']

    # إضافة مدخل المستخدم الحالي إلى المحادثة
    conversation_history.append({"role": "user", "content": prompt})

    # استدعاء API للحصول على الرد
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    # استخراج الرد من الـAPI وتحديث المحادثة
    assistant_reply = response['choices'][0]['message']['content'].strip()
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply


@frappe.whitelist()
def search_and_open_interface(text):
    print("Hello Every Things")
    
    GPT=get_openai_response2(text)

    # return "fff"
    search_link("DocType", text,
    query="frappe.core.report.permitted_documents_for_user.permitted_documents_for_user.query_doctypes",
	filters={"user": "Administrator"},
	page_length=20,
	searchfield=None)
    results = frappe.response["results"]
    # افترض أن النتائج هي قائمة من القواميس (dicts)
    if len(results) > 0:
        text = text.lower()
        text = text.replace(" ", "-")
        
        doctype_name = results[0]["value"]
        # return doctype_name
        doctype_name=doctype_name.lower()
        doctype_name=doctype_name.replace(" ","-")
        # إذا تم العثور على الواجهة، فقم بفتحها
        redirect_url = f"/app/{doctype_name}"
        if(len(results)<0):
            return {
                    "Error":'options',
                    "msg":'سيتم فتح الواجهة',
                    "lang":frappe.local.lang,
                    "results":results
                    }
        else:
            return {"redirect": redirect_url,
                "Error":'true',
                "msg":'سيتم فتح الواجهة',
                "lang":frappe.local.lang   
            }
        
    else:
        return {
            "Error":'false',
            "msg":GPT,
            "lang":frappe.local.lang
        }



