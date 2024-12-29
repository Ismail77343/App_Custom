// const RecordRTC = require('recordrtc');
// وظيفة لإضافة الرسالة تدريجيًا إلى المحادثة
function typeMessage(selector, text, delay = 50) {
    let i = 0;
    function type() {
        if (i < text.length) {
            $(selector).append(text.charAt(i));
            i++;
            setTimeout(type, delay);
        }
    }
    $("#chats-gpt").scrollTop($("#chats-gpt")[0].scrollHeight);
    type();

}
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
// setTimeout(record, 500);



var script = document.createElement('script');
script.src = "https://code.responsivevoice.org/responsivevoice.js?key=SEeTqKsM"; // استبدل YOUR_API_KEY بمفتاح API الخاص بك
document.head.appendChild(script);

// دالة لتحويل النص إلى كلام
function speakText(message, message_eng = "", rec = false) {
    // تحقق مما إذا كانت المكتبة جاهزة
    // alert("Dss");
    playArabicAudio(message,message_eng,rec);
    return 0;
    Speaking=true;
    var voices=[{"ar-SA":"Arabic Female","en-US":"US English Female","en-GB":"UK English Female","es-ES":"Spanish Female","fr-FR":"French Female","de-DE":"US English Female","it-IT":"Italian Female","pt-BR":"Portuguese Female","ru-RU":"Russian Female","zh-CN":"Chinese Female","ja-JP":"Japanese Female","ko-KR":"Korean Female","hi-IN":"Hindi Female","sv-SE":"Swedish Female","pl-PL":"UK English Female","tr-TR":"Turkish Female","da-DK":"UK English Female","no-NO":"Norwegian Female","fi-FI":"UK English Female","cs-CZ":"UK English Female","sk-SK":"Slovak Female","hu-HU":"UK English Female","ro-RO":"Romanian Female","el-GR":"Greek Female","fil-PH":"Filipino Female","bn-BD":"Bangla Bangladesh Female"}]

    if (typeof responsiveVoice !== 'undefined') {
        msg=frappe.boot.lang === "ar" ? message : message_eng;
        var voice=voices[0][selectedlang];//frappe.boot.lang === "ar"?"Arabic Female":"UK English Female";
        running=false;
        console.log("------------");
        console.log("Voice : "+voices[0][selectedlang]);
        
        // playArabicAudio(message,message_eng,rec)

        responsiveVoice.speak(msg, voice, {
            onend: function() {
                $('#chats-gpt').append(`<p ><p align="left">Sara:</p> <p class="chat-sara">${message}</p></p>`);
                $("#chats-gpt").scrollTop($("#chats-gpt")[0].scrollHeight);

                console.log("Finished speaking the text.");
                // هنا يمكنك تنفيذ أي عملية تريدها عند انتهاء الكلام
                // alert("انتهى تحويل النص إلى كلام.");
                if (rec) {
                    // alert("end");
                    // running=true;
                    setTimeout(() => {
                        Speaking = false;
                    }, 1000);
                    setTimeout(record, 1000); // إعادة تشغيل التسجيل بعد تأخير بسيط
                }
            }
        }); // يمكنك تغيير اللغة هنا
    } else {
        console.error("ResponsiveVoice library is not loaded yet.");
        playArabicAudio(message,message_eng,rec)
    }
}
// alert("dds123");
// التفاعل عند النقر على زر بدء التسجيل

const synth = window.speechSynthesis;
var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
var selectedlang=frappe.boot.lang === "ar" ? 'ar-SA' : 'en-US';
if(localStorage.getItem("lang") != null)
    selectedlang=localStorage.getItem("lang");

// alert(frappe.boot.lang);
// وظيفة لتشغيل الرسالة الصوتية
function playArabicAudio(message, message_eng = "", rec = false) {
    Speaking=true;
    // const synth = window.speechSynthesis;
    const utterance = new SpeechSynthesisUtterance(frappe.boot.lang === "ar" ? message : message_eng);
    utterance.lang = selectedlang; //frappe.boot.lang === "ar" ? 'ar-SA' : 'en-US';
    
    // تأكد من بدء التسجيل بعد الانتهاء من تشغيل الرسالة الصوتية
    utterance.onend = function() {
        if (rec) {
            $('#chats-gpt').append(`<p ><p align="left">Sara:</p> <p class="chat-sara">${message}</p></p>`);
            $("#chats-gpt").scrollTop($("#chats-gpt")[0].scrollHeight);
            setTimeout(() => {
                Speaking = false;
            }, 1000);
            // alert("end");
            // running=true;
            setTimeout(record, 1000); // إعادة تشغيل التسجيل بعد تأخير بسيط
        }
    };
    // running=false;
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
    // frappe.msgprint({
    //     message: ' حدث خطأ في التعرف على الصوت'+event.error ,
    //     title: "خطأ",
    //     indicator: "red"
    // });
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
                  speakText("سيتم فتح الواجهة الان", "Ok Dir." + frappe.session.user + ". I will Open Interface Now",rec);
              }else if(response.message.options=="ChangeLang"){
                localStorage.setItem("lang",response.message.lang)
                recognition.stop();
                running=false;
                
                selectedlang = response.message.lang;
                // recognition.continuous = true; // يستمر في الاستماع دون توقف
                // recognition.interimResults = false;
                
                recognition.lang= response.message.lang;
                // recognition.start();

                console.log("Chnaging languge to22: "+selectedlang)
                console.log("Chnaging languge to: "+recognition.lang)
                speakText(response.message.msg, response.message.msg,rec);
                frappe.call({
                    method: "frappe.client.insert",
                    args: {
                        doc: {
                            doctype: "AI Chats",
                            user: frappe.session.user,
                            massge: response.message.msg,
                            speaker: "Sara: ",
    
                        }
                    }
                });
              }
              else if (response.message.Error == "options") {
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
                //   frappe.msgprint(msg);
                  speakText(msg_speach, msg_speach_eng,rec);
                  Recording();
              } else {
                  response.message.msg=response.message.msg.replaceAll("An error occurred while processing your request"," Your question has ended. Please wait 10 minutes and try again. ");

                  frappe.call({
                    method: "frappe.client.insert",
                    args: {
                        doc: {
                            doctype: "AI Chats",
                            user: frappe.session.user,
                            massge: response.message.msg,
                            speaker: "Sara: ",
    
                        }
                    }
                });
                  speakText(response.message.msg, response.message.msg,rec);
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
var Speaking = false;
var startedRec = false;

function record() {
    // speakText("مرحبا بك في نظام ERPALFRAS");

    if ('SpeechRecognition' in window || 'webkitSpeechRecognition' in window) {
        // إعداد التعرف على الصوت
        recognition.continuous = true; // يستمر في الاستماع دون توقف
        recognition.interimResults = false; // لا يعرض النتائج المؤقتة
        recognition.lang = selectedlang; // frappe.boot.lang === "ar" ? 'ar-SA' : 'en-US'; // ضبط اللغة بناءً على إعدادات Frappe
        console.log("lang: "+selectedlang)
        console.log("lang2: "+recognition.lang)
        // معالجة النتائج
        recognition.onresult = function(event) {
            var transcript = event.results[event.results.length - 1][0].transcript;
            console.log("Transcript:", transcript);

            // التحقق من الكلمات المفتاحية
            if ((transcript.includes("أحمد") || transcript.includes("احمد") || transcript.includes("سارة") || transcript.includes("ساره") || transcript.toLowerCase().includes("sara") || transcript.toLowerCase().includes("sarah") || running || $("#chat-box").css("display") !== "none") && !Speaking ) {
                // speakText("نعم انا هنا ماذا تريد", "Yes, I am here. What do you want?", true);
                $("#chat-box").show(); // إظهار صندوق الدردشة إذا كان مخفيًا
                if(transcript.trim()!=""){
                    $("#chat-input").val(transcript); // إدخال النص المنطوق في مربع الدردشة
                    $('#chats-gpt').append(`<p ><p align="right">${frappe.session.user}:</p><p class="chat-me"> ${transcript} </p></p>`);
                    $('#chat-input').val('');
                    $("#chats-gpt").scrollTop($("#chats-gpt")[0].scrollHeight);
                    frappe.call({
                        method: "frappe.client.insert",
                        args: {
                            doc: {
                                doctype: "AI Chats",
                                user: frappe.session.user,
                                massge: transcript,
                                speaker: frappe.session.user,
        
                            }
                        }
                    });
                    running = true;
                    answer(transcript,true);
                }
                // $("#send-message").click(); // إرسال الرسالة
                
            } else if(transcript.includes("توقف") || transcript.toLowerCase().includes("stop")  || transcript.toLowerCase().includes("shutup") || transcript.includes("يكفي كلام")){
                Speaking=false;
                responsiveVoice.cancel();
                window.speechSynthesis.cancel();
                // يمكن إضافة وظيفة للتعامل مع النصوص الأخرى هنا
            }

            // إعادة تعيين startedRec
            startedRec = false;
        };

        // معالجة الأخطاء
        recognition.onerror = function(event) {
            console.log(event.error);
            console.error('Error in speech recognition: ', event.error);
            // frappe.msgprint({
            //     message: 'حدث خطأ في التعرف على الصوت',
            //     title: "خطأ",
            //     indicator: "red"
            // });
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
        }
    }
}

});
