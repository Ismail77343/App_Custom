let mediaRecorder;
let audioChunks = [];
let recordingInterval;

// دالة بدء التسجيل
function startListening() {
    navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
        mediaRecorder = new MediaRecorder(stream);

        // تفعيل الاستماع الدوري كل 5 ثواني
        recordingInterval = setInterval(() => {
            startRecording();
        }, 5000);  // تكرار التسجيل كل 5 ثواني
    }).catch(err => {
        console.error('خطأ في الوصول إلى الميكروفون:', err);
    });
}

// بدء التسجيل لمدة 5 ثواني
function startRecording() {
    if (mediaRecorder && mediaRecorder.state === "recording") {
        console.warn("Recording is already in progress.");
        return;  // إذا كان التسجيل جارياً بالفعل، نخرج من الدالة.
    }

    console.log('بدء التسجيل لمدة 5 ثواني...');
    audioChunks = [];
    
    mediaRecorder.start();

    mediaRecorder.addEventListener("dataavailable", event => {
        audioChunks.push(event.data);
    });

    // إيقاف التسجيل بعد 5 ثواني
    setTimeout(() => {
        stopRecording();
    }, 5000);  // مدة التسجيل 5 ثواني
}

// إيقاف التسجيل وإرسال الصوت إلى السيرفر
function stopRecording() {
    if (mediaRecorder && mediaRecorder.state === "recording") {
        mediaRecorder.stop();
    }else {
        console.warn("No recording is in progress.");
    }
    mediaRecorder.addEventListener("stop", () => {
        const audioBlob = new Blob(audioChunks);
        sendAudioToServer(audioBlob);
    });
}

// إرسال الصوت إلى السيرفر وتحليل النص مع تضمين CSRF Token
function sendAudioToServer(audioBlob) {
    const formData = new FormData();
    formData.append("audio", audioBlob, "audio.wav");

    
    // الحصول على CSRF token من الصفحة
    const csrfToken = frappe.csrf_token;

    fetch("/api/method/alfrasapp.gpt.test.transcribe_audio", {
        method: "POST",
        headers: {
            "X-Frappe-CSRF-Token": csrfToken  // إضافة CSRF Token إلى الهيدر
        },
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log("النص المسجل:", data);
        // عرض الرسالة في صفحة الويب
        // alert(`النص المسجل: ${data}`);
    })
    .catch(error => {
        console.error("خطأ في معالجة الصوت:", error);
    });
}
function stopListening() {
    clearInterval(recordingInterval);
    console.log("تم إيقاف الاستماع الدوري.");
}

// بدء عملية الاستماع عند تحميل الصفحة
// document.addEventListener('DOMContentLoaded', (event) => {
//     startListening();
//     stopListening();
// });
