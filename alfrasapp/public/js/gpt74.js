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
setTimeout(record, 500);


// التفاعل عند النقر على زر بدء التسجيل

const synth = window.speechSynthesis;
var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

// وظيفة لتشغيل الرسالة الصوتية
function playArabicAudio(message, message_eng = "", rec = false) {
    const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(frappe.boot.lang === "ar" ? message : message_eng);
    utterance.lang = frappe.boot.lang === "ar" ? 'ar-SA' : 'en-US';
    
    // تأكد من بدء التسجيل بعد الانتهاء من تشغيل الرسالة الصوتية
    utterance.onend = function() {
        if (rec) {
            // alert("end");
            // running=true;
            setTimeout(record, 1000); // إعادة تشغيل التسجيل بعد تأخير بسيط
        }
    };
    running=false;
    synth.speak(utterance);
}

function Recording(){
if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {


// استخدام الوظيفة
// const arabicMessage = 'مرحبًا، هذه رسالة صوتية باللغة العربية.';
// playArabicAudio(arabicMessage);
// console.log(arabicMessage);
// إنشاء مثيل من واجهة التعرف على الصوت
// const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();

// تعيين لغة التعرف إلى اللغة المناسبة
frappe.boot.lang;
if(frappe.boot.lang=="ar")
recognition.lang = 'ar-SU';
else
recognition.lang = 'en-US';

// التعرف على النص من الصوت
recognition.onresult = function(event) {
  var transcript = event.results[0][0].transcript;
  answer(transcript)
 
};

// التعرف على الأخطاء في التعرف على الصوت
recognition.onerror = function(event) {
    console.error('حدث خطأ في التعرف على الصوت: '+event.error, event.error);
    frappe.msgprint({
        message: ' حدث خطأ في التعرف على الصوت'+event.error ,
        title: "خطأ",
        indicator: "red"
    });
};
// إعادة تشغيل التسجيل بعد انتهاء
recognition.onend = function() {
    startedRec = false;
    if (!running) {
        setTimeout(() => record(), 1000); // إعادة بدء التسجيل بعد تأخير بسيط
    }
};

    // recognition.start();
    if(!startedRec){
        recognition.start();
        startedRec==true;
    }

}
}

function answer(transcript,rec=false){
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
                  response.message.redirect=response.message.redirect.replaceAll("`","");
                  window.location = response.message.redirect.trim();

                  console.log(response.message.redirect+" : ")
                  console.log(response.message.redirect.trim()+" : ")
                  playArabicAudio("سيتم فتح الواجهة الان", "Ok Dir." + frappe.session.user + ". I will Open Interface Now",rec);
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
                  playArabicAudio(msg_speach, msg_speach_eng,rec);
                  Recording();
              } else {
                  response.message.msg=response.message.msg.replaceAll("An error occurred while processing your request"," Your question has ended. Please wait 10 minutes and try again. ");
                  playArabicAudio(response.message.msg, response.message.msg,rec);
              }
          } else {
            
              console.error("Error field is missing in the response");
          }
      }
  
  
  });
  
  startedRec==false;
  
      // عرض النص في رسالة Frappe
      // frappe.msgprint({
      //     message: transcript,
      //     title: "النص المحول",
      //     indicator: "green"
      // });
}
var running = false;
var startedRec = false;

function record() {
    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
        // إعداد التعرف على الصوت
        recognition.continuous = true; // يستمر في الاستماع دون توقف
        recognition.interimResults = false; // لا يعرض النتائج المؤقتة
        recognition.lang = frappe.boot.lang === "ar" ? 'ar-SA' : 'en-US'; // ضبط اللغة بناءً على إعدادات Frappe

        // معالجة النتائج
        recognition.onresult = function(event) {
            var transcript = event.results[event.results.length - 1][0].transcript;
            console.log("Transcript:", transcript);

            // التحقق من الكلمات المفتاحية
            if (transcript.includes("أحمد") || transcript.includes("احمد") || transcript.includes("سارة") || transcript.includes("ساره") || transcript.toLowerCase().includes("sara") || running) {
                // playArabicAudio("نعم انا هنا ماذا تريد", "Yes, I am here. What do you want?", true);
                $("#chat-box").show(); // إظهار صندوق الدردشة إذا كان مخفيًا
                $("#chat-input").val(transcript); // إدخال النص المنطوق في مربع الدردشة
                // $("#send-message").click(); // إرسال الرسالة
                running = true;
                answer(transcript,true);
            } else if(transcript.includes("توقف") || transcript.includes("stop") || transcript.includes("يكفي كلام")){
                window.speechSynthesis.cancel();

                // يمكن إضافة وظيفة للتعامل مع النصوص الأخرى هنا
            }

            // إعادة تعيين startedRec
            startedRec = false;
        };

        // معالجة الأخطاء
        recognition.onerror = function(event) {
            console.error('Error in speech recognition: ', event.error);
            frappe.msgprint({
                message: 'حدث خطأ في التعرف على الصوت',
                title: "خطأ",
                indicator: "red"
            });
            startedRec = false;
        };

        // إعادة تشغيل التسجيل بعد انتهاء
        recognition.onend = function() {
            startedRec = false;
            if (!running) {
                setTimeout(() => record(), 1000); // إعادة بدء التسجيل بعد تأخير بسيط
            }
        };

        // بدء التسجيل
        if (!startedRec) {
            recognition.start();
            startedRec = true;
        }4
    }
}

});
