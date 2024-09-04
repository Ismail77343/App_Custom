import frappe
# import speech_recognition as sr
# import pyaudio
import frappe.desk.search
from frappe import whitelist
from frappe.desk.search import search_link
import json

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



    
@frappe.whitelist()
def search_and_open_interface(text):
    print("Hello Every Things")
    
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
            "msg":'لم يتم العثور على أي نتائج',
            "lang":frappe.local.lang
        }



