// const RecordRTC = require('recordrtc');

document.addEventListener('DOMContentLoaded', function() {
    function rotatimage(){
  // alert("dssd");
  var isRTL = getComputedStyle(document.body).direction === "rtl";
  var rtlImage = document.getElementById("rtl-image");

  if(document.getElementById("rtl-image")){
    if (isRTL) {
      rtlImage.style.transform = "rotate(180deg)";
    } else {
      rtlImage.style.transform = "rotate(0deg)";
    }
  }else{
    setTimeout(rotatimage, 500);
  }
  
}
function addCustomButton() {
    // تحقق مما إذا كان شريط التنقل جاهزًا
    if (document.querySelector('.navbar .container')) {
        // إنشاء زر بدء التسجيل
        var startButton = document.createElement('button');
        startButton.innerHTML = '';
        startButton.className = 'btn btn-primary navbar-btn fa fa-microphone';
        startButton.id = 'startRecording';
        
        // إضافة الزر إلى شريط التنقل
        var container = document.querySelector('.navbar .container');
        container.appendChild(startButton);

        startButton.addEventListener('click', function() {
            // const recognition = new webkitSpeechRecognition();
            // recognition.continuous = true;
            // recognition.interimResults = true;
            // recognition.lang = 'en-US';

            // const startRecording = () => {
            //     recognition.start();
            //     recognition.onresult = (event) => {
            //         const transcript = event.results[event.results.length - 1][0].transcript;
            //         console.log(transcript); // عرض النص المحول
            //     };
            // };

            // const stopRecording = () => {
            //     recognition.stop();
            // };

            Recording();
            
                // بدء التسجيل
                // توجيه التسجيل إلى ملف صوتي أو إلى المتغير الذي تريده
                // إرسال طلب إلى الخادم لبدء تسجيل الصوت
                // frappe.call({
                //     method: 'alfrasgpt.api.start_audio_recording',
                //     callback: function(response) {
                //         if (response.message) {
                //             frappe.msgprint(response.message);
                //         }
                //     }
                // });

            

        });
        
    } else {
        // إذا لم يكن جاهزًا، تحقق مرة أخرى بعد 500 مللي ثانية
        setTimeout(addCustomButton, 500);
    }
}

// بدء المحاولة لإضافة الزر بعد تحميل الصفحة
setTimeout(addCustomButton, 500);
setTimeout(rotatimage, 500);

// التفاعل عند النقر على زر بدء التسجيل


function Recording(){
if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
const synth = window.speechSynthesis;

// وظيفة لتشغيل الرسالة الصوتية
function playArabicAudio(message,message_eng="") {
  // إنشاء utterance جديد
  lang="en-US";
  msg=message_eng;
  if(frappe.boot.lang=="ar"){
    lang = 'ar-SA';
    msg=message;
  }
  
  const utterance = new SpeechSynthesisUtterance(msg);

  utterance.lang=lang;
  // تعيين اللغة إلى العربية
  // utterance.lang = 'ar-SA';

  // تشغيل الرسالة الصوتية
  synth.speak(utterance);
}

// استخدام الوظيفة
// const arabicMessage = 'مرحبًا، هذه رسالة صوتية باللغة العربية.';
// playArabicAudio(arabicMessage);
// console.log(arabicMessage);
// إنشاء مثيل من واجهة التعرف على الصوت
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

// تعيين لغة التعرف إلى اللغة المناسبة
frappe.boot.lang;
if(frappe.boot.lang=="ar")
recognition.lang = 'ar-SU';
else
recognition.lang = 'en-US';

// التعرف على النص من الصوت
recognition.onresult = function(event) {
  var transcript = event.results[0][0].transcript;
  // البحث عن النص في الصفحة
  
  //   frappe.call({
  //     method: 'frappe.desk.search.search_widget',
  //     args: {
  //         doctype: '', // يمكنك تحديد نوع المستند الذي ترغب في البحث فيه إذا كان لديك نوع محدد
  //         txt: transcript,
  //         filters: {}  // يمكنك إضافة عوامل التصفية إذا كنت بحاجة
  //     },
  //     callback: function(response) {
  //         if (response.message) {
  //             // التعامل مع نتائج البحث
  //             console.log(response.message);
  //             // يمكنك عرض النتائج بطريقة تناسب تطبيقك
  //             frappe.msgprint({
  //                 message: JSON.stringify(response.message),
  //                 title: "نتائج البحث",
  //                 indicator: "green"
  //             });
  //         } else {
  //             frappe.msgprint({
  //                 message: "لم يتم العثور على نتائج",
  //                 title: "نتائج البحث",
  //                 indicator: "red"
  //             });
  //         }
  //     }
  // });
  document.getElementById("navbar-search").value=transcript;
  
  
  
  // transcript=transcript.replaceAll("العميل","عميل");
  // transcript=transcript.replaceAll("العملاء","عميل");
  // transcript=transcript.replaceAll("الموردون","مورد");
  // transcript=transcript.replaceAll("المورد","مورد");
  // transcript=transcript.replaceAll("واجهة","قائمة");
  // transcript=transcript.replaceAll("واجهه","");
  // transcript=transcript.replaceAll("واجهات","");
  // transcript=transcript.replaceAll("افتح","");
  // transcript=transcript.replaceAll("open","");
  // transcript=transcript.replaceAll("interface","list");
  frappe.call({
    method: 'alfrasapp.gpt.gpt.StartGPT',
    args: {
        text: transcript,
    },
    callback: function(response) {
        console.log(response);  // تحقق من أن البيانات المستلمة صحيحة

        function getDomainName() {
            const url = new URL(window.location.href);
            return url.hostname;
        }

        if (response.message && response.message.Error) {
            if (response.message.Error == "true") {
                window.location = response.message.redirect.trim();
                console.log(response.message.redirect+" : ")
                console.log(response.message.redirect.trim()+" : ")
                playArabicAudio("سيتم فتح الواجهة الان", "Ok Dir." + frappe.session.user + ". I will Open Interface Now");
            } else if (response.message.Error == "options") {
                console.log(response.message.results);
                var msg = "<ol>";
                var m = "";
                for (let i = 0; i < response.message.results.length; i++) {
                    const element = response.message.results[i];
                    var element_href = element.value.toLowerCase();
                    m += (i + 1) + " " + element.value;
                    element_href = element_href.replaceAll(" ", "-");
                    msg += "<li><a href='/app/" + element_href + "'> " + element.value + "</a></li>";
                }
                msg += "</ol>";

                var msg = "هناك الكثير من الواجهات بهذا الاسم حدد اي من هذه الواجهات تريد" + msg;
                var msg_eng = "There are many interfaces with this name. Select which of these interfaces you want" + msg;
                var msg_speach = "هناك الكثير من الواجهات بهذا الاسم حدد اي من هذه الواجهات تريد" + m;
                var msg_speach_eng = "There are many interfaces with this name. Select which of these interfaces you want" + m;
                msg = frappe.boot.lang == "ar" ? msg : msg_eng;
                response.message.msg=response.message.msg.replaceAll("An error occurred while processing your request"," Your question has ended. Please wait 10 minutes and try again. ");
                frappe.msgprint(msg);
                playArabicAudio(msg_speach, msg_speach_eng);
                Recording();
            } else {
                response.message.msg=response.message.msg.replaceAll("An error occurred while processing your request"," Your question has ended. Please wait 10 minutes and try again. ");
                playArabicAudio(response.message.msg, response.message.msg);
            }
        } else {
          
            console.error("Error field is missing in the response");
        }
    }
});


    // عرض النص في رسالة Frappe
    // frappe.msgprint({
    //     message: transcript,
    //     title: "النص المحول",
    //     indicator: "green"
    // });
};

// التعرف على الأخطاء في التعرف على الصوت
recognition.onerror = function(event) {
    console.error('حدث خطأ في التعرف على الصوت: ', event.error);
    frappe.msgprint({
        message: 'حدث خطأ في التعرف على الصوت',
        title: "خطأ",
        indicator: "red"
    });
};

// بدء التعرف على الصوت عند الضغط على الزر مثلاً
// document.getElementById('startRecordingButton').addEventListener('click', function() {
    recognition.start();
// });

}
}
});
