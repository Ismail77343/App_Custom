import frappe
import whisper
import os

@frappe.whitelist(allow_guest=True)
def transcribe_audio():
    # استلام ملف الصوت من الطلب
    file = frappe.request.files.get('audio')
    if not file:
        return {'error': 'No audio file uploaded'}
    
    file_path = "audio.wav"
    
    # حفظ الملف مؤقتًا
    file.save(file_path)
    
    # استخدام Whisper لتحويل الصوت إلى نص
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    
    # حذف الملف المؤقت
    os.remove(file_path)
    
    return {'text': result['text']}
