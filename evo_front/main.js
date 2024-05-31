$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn"
        },
        out:{
            effect: "bounceOut"
        }
    });
    //Evo Wave configuration
    var siriWave = new SiriWave({
        container: document.getElementById("evo-wave"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed : "0.2",
        autostart: true
    });
    //Evo message animation
    $('.evo-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "fadeInUp",
            sync: true,
        },
        out:{
            effect: "fadeOutUp",
            sync: true,
        }
    });
    //Mic button click event
    $("#MicBtn").click(function () { 
        eel.playEvoSound()
        $("#Oval").attr("hidden", true);
        $("#EvoWave").attr("hidden", false);
        eel.allCommands()()
    });
    function doc_keyUp(e){
        if(e.key === 'v' && e.ctrlKey){
            eel.playEvoSound()
            $("#Oval").attr("hidden", true);
            $("#EvoWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // to play assisatnt 
    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").attr("hidden", true);
            $("#EvoWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }

    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // key up event handler on text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)
    
    });
    
    // send button event handler
    $("#SendBtn").click(function () {
    
        let message = $("#chatbox").val()
        PlayAssistant(message)
    
    });

    // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });

});
