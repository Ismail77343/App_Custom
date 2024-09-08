document.addEventListener('DOMContentLoaded', function() {
    // alert("ss")
    // وظيفة لتشغيل الرسالة الصوتية



const synth = window.speechSynthesis;

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

  
    // إضافة الويدجت عند تحميل الصفحة
    $('body').append(`
        <div id="chat-widget" style="position: fixed; bottom: 20px; right: 20px; z-index: 999;">
            <button id="open-chat" style="background-color: #0788c9; color: white; border: none; padding: 10px 20px; border-radius: 50px;">
                <i class="fa fa-comments"></i> Talk With Us
            </button>
            <div id="chat-box" style="display: none; background-color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px; width: 300px; max-height: 400px; overflow: auto;">
                <div style="padding: 10px; text-align: center;">
                    <h4>Your Assistant</h4>
                    <img src="/assets/alfrasapp/images/roboot.png" style='width:40%;display:block;margin:auto;'/>
                </div>
                <div style="padding: 10px;">
                    <textarea id="chat-input" placeholder="Type your message..." style="width: 100%; height: 50px;"></textarea>
                    <button id="send-message" style="width: 100%; padding: 10px; background-color: #0788c9; color: white; border: none;">Send</button>
                </div>
            </div>
        </div>
    `);

    // أحداث الويدجت
    $('#open-chat').on('click', function() {
        $('#chat-box').toggle();
        window.speechSynthesis.cancel();
    });

    $('#send-message').on('click', function() {
        let message = $('#chat-input').val();
        $('#chat-box').append(`<p><b>Me:</b> ${message}</p>`);
        if (message) {
            frappe.call({
                method: "alfrasapp.gpt.gpt.StartGPT",
                args: { text: message },
                callback: function(response) {
                    if (response.message && response.message.Error) {
                        if (response.message.Error == "true") {
                            window.location = response.message.redirect.trim();
                            console.log(response.message.redirect+" : ")
                            console.log(response.message.redirect.trim()+" : ")
                            playArabicAudio("سيتم فتح الواجهة الان", "Ok Dir." + frappe.session.user + ". I will Open Interface Now");
                        }else{
                            $('#chat-box').append(`<p><b>Sara:</b> ${response.message.msg}</p>`);
                            $('#chat-input').val('');
                        }
                    }else{
                        $('#chat-box').append(`<p><b>Wraning:</b> Your Limit Is Finsh Please Try Agine After 10m</p>`);
                    }
                }
            });
        }
    });


});
