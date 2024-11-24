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
  
    // إضافة الويدجت عند تحميل الصفحة
    $('body').append(`
        <div id="chat-widget" style="">
            <button id="open-chat" style="background-color: #0788c9; color: white; border: none; padding: 10px 20px; border-radius: 50px;">
                <i class="fa fa-comments"></i> Talk With AI
            </button>
            <div id="chat-box" style="display: none; background-color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.1); border-radius: 10px; width: 300px;  ">
                
                <div style="padding: 10px; text-align: center;">
                    <h4>Your Assistant</h4>
                    <img src="/assets/alfrasapp/images/roboot.png" style='width:30%;display:block;margin:auto;'/>
                </div>
                <div id="chats-gpt" style="max-height:220px;overflow: auto;border-radius: 10px;height:220px;" ></div>
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
        responsiveVoice.cancel();
        window.speechSynthesis.cancel();
        $("#chats-gpt").scrollTop($("#chats-gpt")[0].scrollHeight);

    });

    $('#send-message').on('click', function() {
        let message = $('#chat-input').val();
        $('#chats-gpt').append(`<p ><p align="right">${frappe.session.user}</p ><p class="chat-me"> ${message}</p></p>`);
        $("#chats-gpt").scrollTop($("#chats-gpt")[0].scrollHeight);

        if (message) {
            frappe.call({
                method: "frappe.client.insert",
                args: {
                    doc: {
                        doctype: "AI Chats",
                        user: frappe.session.user,
                        massge: message,
                        speaker: frappe.session.user,

                    }
                }
            });
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
                            $('#chats-gpt').append(`<p ><p align="left">Sara:</p> <p class="chat-sara"></p></p>`);
                            $('#chat-input').val('');
                            typeMessage('.chat-sara:last', response.message.msg);
                            $("#chats-gpt").scrollTop($("#chats-gpt")[0].scrollHeight);
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
                    }else{
                        $('#chats-gpt').append(`<p><b>Wraning:</b> Your Limit Is Finsh Please Try Agine After 10m</p>`);
                        $("#chats-gpt").scrollTop($("#chats-gpt")[0].scrollHeight);

                    }
                }
            });
        }
    });

    function getlist(){
        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "AI Chats",
                fields: ["speaker", "massge", "user"],
                filters: {
                    user: frappe.session.user
                },
                limit_page_length: 20,
                order_by: "creation desc"
            },
            callback: function(response) {
                if (response.message) {
                    // ترتيب الرسائل بحيث تظهر الأحدث في الأسفل
                    let messages = response.message.reverse();
                    
                    for (let I = 0; I < messages.length; I++) {
                        const chat = messages[I];
                        // alert("dsd: "+messages.length);
                        console.log("Chats AI: ");
                        console.log(messages);
                        if (chat.massge != "" && chat.massge != null) {
                            cls=chat.speaker=="Sara: "?"chat-sara":"chat-me";
                            align=chat.speaker=="Sara: "?"left":"right";
                            $('#chats-gpt').append(
                                `<p><p align="${align}">${chat.speaker}</p><p class="${cls}">${chat.massge}</p></p>`
                            );

                        }
                    }
                    // عرض الرسائل في واجهة المحادثة
                    // messages.forEach(function(chat) {
                    //     alert("dsd");
                    //     console.log("Chats AI: ");
                    //     console.log(messages);
                    //     if (chat.massge.trim() != "") {
                    //         $('#chats-gpt').append(
                    //             `<p><p align="right">${chat.speaker}:</p><p class="chat-me">${chat.massge}</p></p>`
                    //         );
    
                    //     }
                    // });
    
                    // التمرير إلى آخر رسالة بعد تحميل الرسائل
                    // $("#chats-gpt").scrollTop($("#chats-gpt")[0].scrollHeight);
                }
            }
        });
    }
    setTimeout(() => getlist(), 500);

});
